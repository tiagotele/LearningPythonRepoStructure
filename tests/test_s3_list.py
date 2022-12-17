import os
import pytest
import boto3
from moto import mock_s3
from tempfile import NamedTemporaryFile

from s3_list_buckets.s3_list import MyS3Client


@pytest.fixture
def bucket_name():
    return "my-test-bucket"


@pytest.fixture
def s3_test(s3_client, bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)
    yield


@pytest.fixture
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture
def s3_client(aws_credentials):
    with mock_s3():
        conn = boto3.Session().client("s3", region_name="us-east-1")
        yield conn


def test_list_buckets(s3_client, s3_test):
    my_client = MyS3Client()
    buckets = my_client.list_buckets()
    assert buckets == ["my-test-bucket"]


def test_list_objects(s3_client, s3_test, bucket_name):
    file_text = "test"
    with NamedTemporaryFile(delete=True, suffix=".txt") as tmp:
        with open(tmp.name, "w", encoding="UTF-8") as f:
            f.write(file_text)

        s3_client.upload_file(tmp.name, bucket_name, "file12")
        s3_client.upload_file(tmp.name, bucket_name, "file22")

    my_client = MyS3Client()
    objects = my_client.list_objects(bucket_name=bucket_name, prefix="file1")
    assert objects == ["file12"]


def test_download_file(s3_client, s3_test, bucket_name):
    file_text = "test"
    with NamedTemporaryFile(delete=True, suffix=".txt") as tmp:
        with open(tmp.name, "w", encoding="UTF-8") as f:
            f.write(file_text)
        s3_client.upload_file(tmp.name, bucket_name, "test")

    my_client = MyS3Client()
    my_client.download_file(bucket_name, "test", "downloaded_file.txt")

    assert os.path.isfile("downloaded_file.txt")
