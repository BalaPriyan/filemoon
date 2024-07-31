# FileMoon API Python Wrapper

This is a Python wrapper for the FileMoon API. It allows you to interact with various endpoints of the FileMoon service to manage files, accounts, and other related operations.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Methods](#methods)
  - [Account Information](#account-information)
  - [Account Statistics](#account-statistics)
  - [DMCA List](#dmca-list)
  - [Deleted Files List](#deleted-files-list)
  - [Remote Upload](#remote-upload)
  - [Remove Remote Upload](#remove-remote-upload)
  - [Remote Upload Status](#remote-upload-status)
  - [File Information](#file-information)
  - [File List](#file-list)
  - [Clone File](#clone-file)
  - [Folder List](#folder-list)
  - [Create Folder](#create-folder)
  - [Encoding Operations](#encoding-operations)
  - [Image Operations](#image-operations)
  - [Video Preview](#video-preview)

## Installation

```bash
pip install requests
```

## Usage

```python
from filemoon import FileMoon

# Initialize with your API key
filemoon = FileMoon(api_key='YOUR_API_KEY')

# Get account info
info = filemoon.account_info()
print(info)
```

## Methods

### Account Information

<details>
  <summary>Get basic info of your account</summary>

```python
info = filemoon.account_info()
print(info)
```

</details>

### Account Statistics

<details>
  <summary>Get reports of your account (default last 7 days)</summary>

```python
stats = filemoon.account_stats(last='7')
print(stats)
```

</details>

### DMCA List

<details>
  <summary>Get DMCA reported files list (500 results per page)</summary>

```python
dmca = filemoon.dmca_list(last='7')
print(dmca)
```

</details>

### Deleted Files List

<details>
  <summary>Get deleted files list (500 results per page)</summary>

```python
deleted = filemoon.deleted_list(last='7')
print(deleted)
```

</details>

### Remote Upload

<details>
  <summary>Upload files using direct links</summary>

```python
upload = filemoon.remote_upload(direct_link='https://example.com/file.mp4')
print(upload)
```

Optional parameter `fld_id` can be used to specify the folder ID.

```python
upload = filemoon.remote_upload(direct_link='https://example.com/file.mp4', fld_id='FOLDER_ID')
print(upload)
```

</details>

### Remove Remote Upload

<details>
  <summary>To remove remote upload</summary>

```python
remove = filemoon.reremote_upload(file_code='FILE_CODE')
print(remove)
```

</details>

### Remote Upload Status

<details>
  <summary>To check remote upload status</summary>

```python
status = filemoon.remote_upload_status(file_code='FILE_CODE')
print(status)
```

</details>

### File Information

<details>
  <summary>To get file information</summary>

```python
file_info = filemoon.file_info(file_code='FILE_CODE')
print(file_info)
```

</details>

### File List

<details>
  <summary>To list files</summary>

```python
file_list = filemoon.file_list(name='example', per_page='10', page='1')
print(file_list)
```

Optional parameters:
- `fld_id`: Folder ID to list files from
- `name`: To fetch a file by name
- `created`: To fetch by created date
- `public`: To fetch by public media
- `per_page`: To fetch by per page
- `page`: To fetch by page

</details>

### Clone File

<details>
  <summary>To clone a file</summary>

```python
clone = filemoon.clone_file(file_code='FILE_CODE')
print(clone)
```

Optional parameter `fld_id` can be used to specify the folder ID.

```python
clone = filemoon.clone_file(file_code='FILE_CODE', fld_id='FOLDER_ID')
print(clone)
```

</details>

### Folder List

<details>
  <summary>To get folder list</summary>

```python
folders = filemoon.folder_list(fld_id='FOLDER_ID')
print(folders)
```

Optional parameter `fld_id` can be used to specify the folder ID.

</details>

### Create Folder

<details>
  <summary>To create a folder</summary>

```python
new_folder = filemoon.create_folder(name='New Folder')
print(new_folder)
```

Optional parameter `parent_id` can be used to specify the parent folder ID.

```python
new_folder = filemoon.create_folder(name='New Folder', parent_id='PARENT_ID')
print(new_folder)
```

</details>

### Encoding Operations

<details>
  <summary>Get encoding list</summary>

```python
encoding_list = filemoon.encode_list()
print(encoding_list)
```

</details>

<details>
  <summary>Get encoding status</summary>

```python
status = filemoon.encode_status(file_code='FILE_CODE')
print(status)
```

</details>

<details>
  <summary>Restart encoding error files</summary>

```python
restart = filemoon.restart_encode_error(file_code='FILE_CODE')
print(restart)
```

</details>

<details>
  <summary>Delete encoding error files</summary>

```python
delete = filemoon.delete_encode_error(file_code='FILE_CODE')
print(delete)
```

</details>

### Image Operations

<details>
  <summary>Get thumbnail image URL</summary>

```python
thumbnail = filemoon.thumb(file_code='FILE_CODE')
print(thumbnail)
```

</details>

<details>
  <summary>Get splash image</summary>

```python
splash = filemoon.splash(file_code='FILE_CODE')
print(splash)
```

</details>

### Video Preview

<details>
  <summary>Get video preview of specific file</summary>

```python
preview = filemoon.vid_preview(file_code='FILE_CODE')
print(preview)
```

</details>

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues and pull requests to improve the codebase. All contributions are welcome!

## Author

Your Name - [BalaPriyan](https://github.com/BalaPriyan)
