from types import SimpleNamespace
import unittest
from unittest.mock import MagicMock, patch

from lncrawl.exceptions import ServerErrors
from lncrawl.server.api import jobs as jobs_api
from lncrawl.server.models import FetchMissingRequest
from lncrawl.services.jobs import service as job_service_module
from lncrawl.services.jobs.service import JobService


class TestFetchMissingChapters(unittest.TestCase):
    def make_ctx(self, chapters):
        novel = SimpleNamespace(id="novel-1", title="Novel Title")
        return SimpleNamespace(
            novels=SimpleNamespace(get=MagicMock(return_value=novel)),
            chapters=SimpleNamespace(list=MagicMock(return_value=chapters)),
        )

    def chapter(self, chapter_id, available):
        return SimpleNamespace(id=chapter_id, is_available=available)

    def test_mixed_availability_delegates_only_missing_ids(self):
        service = JobService()
        user = object()
        job = object()
        ctx = self.make_ctx(
            [
                self.chapter("available-1", True),
                self.chapter("missing-1", False),
                self.chapter("missing-2", False),
                self.chapter("available-2", True),
            ]
        )

        with patch.object(job_service_module, "ctx", ctx):
            with patch.object(service, "fetch_many_chapters", return_value=job) as fetch_many:
                with patch.object(service, "fetch_chapter") as fetch_one:
                    result = service.fetch_missing_chapters(user, "novel-1")

        self.assertIs(result, job)
        ctx.novels.get.assert_called_once_with("novel-1")
        ctx.chapters.list.assert_called_once_with(novel_id="novel-1")
        fetch_many.assert_called_once_with(
            user,
            "missing-1",
            "missing-2",
            parent_id=None,
            depends_on=None,
            novel_id="novel-1",
            novel_title="Novel Title",
        )
        fetch_one.assert_not_called()

    def test_single_missing_delegates_fetch_chapter(self):
        service = JobService()
        user = object()
        job = object()
        ctx = self.make_ctx(
            [
                self.chapter("available-1", True),
                self.chapter("missing-1", False),
                self.chapter("available-2", True),
            ]
        )

        with patch.object(job_service_module, "ctx", ctx):
            with patch.object(service, "fetch_chapter", return_value=job) as fetch_one:
                with patch.object(service, "fetch_many_chapters") as fetch_many:
                    result = service.fetch_missing_chapters(user, "novel-1")

        self.assertIs(result, job)
        fetch_one.assert_called_once_with(
            user,
            "missing-1",
            parent_id=None,
            depends_on=None,
            novel_id="novel-1",
            novel_title="Novel Title",
        )
        fetch_many.assert_not_called()

    def test_all_available_raises_and_creates_no_job(self):
        service = JobService()
        user = object()
        ctx = self.make_ctx(
            [
                self.chapter("available-1", True),
                self.chapter("available-2", True),
            ]
        )

        with patch.object(job_service_module, "ctx", ctx):
            with patch.object(service, "fetch_chapter") as fetch_one:
                with patch.object(service, "fetch_many_chapters") as fetch_many:
                    with patch.object(service, "_create") as create:
                        with self.assertRaises(type(ServerErrors.no_chapters_to_download)) as err:
                            service.fetch_missing_chapters(user, "novel-1")

        self.assertIs(err.exception, ServerErrors.no_chapters_to_download)
        fetch_one.assert_not_called()
        fetch_many.assert_not_called()
        create.assert_not_called()

    def test_route_delegates_to_service(self):
        user = object()
        job = object()
        jobs = SimpleNamespace(fetch_missing_chapters=MagicMock(return_value=job))

        with patch.object(jobs_api, "ctx", SimpleNamespace(jobs=jobs)):
            result = jobs_api.fetch_missing(
                user=user,
                body=FetchMissingRequest(novel_id="novel-1"),
            )

        self.assertIs(result, job)
        jobs.fetch_missing_chapters.assert_called_once_with(user, "novel-1")


if __name__ == "__main__":
    unittest.main()
