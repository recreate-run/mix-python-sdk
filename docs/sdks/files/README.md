# Files
(*files*)

## Overview

### Available Operations

* [list_session_files](#list_session_files) - List session files
* [upload_session_file](#upload_session_file) - Upload file to session
* [delete_session_file](#delete_session_file) - Delete session file
* [get_session_file](#get_session_file) - Get session file

## list_session_files

List all files in session storage directory

### Example Usage

<!-- UsageSnippet language="python" operationID="listSessionFiles" method="get" path="/api/sessions/{id}/files" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.files.list_session_files(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.FileInfo]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 404                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## upload_session_file

Upload a file to session-specific storage directory

### Example Usage

<!-- UsageSnippet language="python" operationID="uploadSessionFile" method="post" path="/api/sessions/{id}/files/upload" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.files.upload_session_file(id="<id>", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID                                                          |
| `file`                                                              | [models.File](../../models/file.md)                                 | :heavy_check_mark:                                                  | File to upload                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileInfo](../../models/fileinfo.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 404, 413          | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_session_file

Delete a specific file from session storage. Only files are supported - directories cannot be deleted.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSessionFile" method="delete" path="/api/sessions/{id}/files/{filename}" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    mix.files.delete_session_file(id="<id>", filename="example.file")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID                                                          |
| `filename`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Filename to delete                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 404               | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## get_session_file

Download or serve a specific file from session storage. Supports thumbnail generation with ?thumb parameter.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSessionFile" method="get" path="/api/sessions/{id}/files/{filename}" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.files.get_session_file(id="<id>", filename="example.file")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | Session ID                                                            |
| `filename`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | Filename to retrieve                                                  |
| `thumb`                                                               | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Thumbnail specification: '100' (box), 'w100' (width), 'h100' (height) |
| `time`                                                                | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | Time offset in seconds for video thumbnails (default: 1.0)            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 404               | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |