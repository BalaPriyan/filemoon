# <h1 align="center"><a href="https://filemoon.sx">FileMoon</a></h1>

FileMoon is a video hosting service were you can upload videos, share & make money.

Don't Have Account? Register <a href="https://filemoon.sx/register">Here</a>

<h2>Features</h2>
 - HLS Streaming
 - Unlimited Storage
 - Faster Encoding
 - Subtitles Support
 - Premium bandwidth

 <hr style="border-top: 3px solid #000;">


# <h1 align="center"><a href="https://filemoon.sx">FileMoon</a> API Python Wrapper</h1>

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
  - [Remote Subtitle Management](#remote-subtitle-management)
  - [Server Management](#server-management)

## Installation

```bash
pip install filemoon
```

## Usage

```python
from filemoon import FileMoon

# Initialize with your API key
filemoon = FileMoon(api_key='YOUR_API_KEY')

# Get account info
info = filemoon.info()
print(info)
```

## Methods

### Account Information

<details>
  <summary>Get basic info of your account</summary>

```python
info = filemoon.info()
print(info)
```

</details>

### Account Statistics

<details>
  <summary>Get reports of your account (default last 7 days)</summary>

```python
stats = filemoon.stats(last='7')
print(stats)
```

</details>

### DMCA List

<details>
  <summary>Get DMCA reported files list (500 results per page)</summary>

```python
dmca = filemoon.dmca(last='7')
print(dmca)
```

</details>

### Deleted Files List

<details>
  <summary>Get deleted files list (500 results per page)</summary>

```python
deleted = filemoon.deleted(last='7')
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
remove = filemoon.remove_rup(file_code='FILE_CODE')
print(remove)
```

</details>

### Remote Upload Status

<details>
  <summary>To check remote upload status</summary>

```python
status = filemoon.rup_status(file_code='FILE_CODE')
print(status)
```

</details>

### File Information

<details>
  <summary>To get file information</summary>

```python
f_info = filemoon.f_info(file_code='FILE_CODE')
print(f_info)
```

</details>

### File List

<details>
  <summary>To list files</summary>

```python
f_list = filemoon.f_list(name='example', per_page='10', page='1')
print(f_list)
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
clone = filemoon.clone_f(file_code='FILE_CODE')
print(clone)
```

Optional parameter `fld_id` can be used to specify the folder ID.

```python
clone = filemoon.clone_f(file_code='FILE_CODE', fld_id='FOLDER_ID')
print(clone)
```

</details>

### Folder List

<details>
  <summary>To get folder list</summary>

```python
folders = filemoon.fld_list(fld_id='FOLDER_ID')
print(folders)
```

Optional parameter `fld_id` can be used to specify the folder ID.

</details>

### Create Folder

<details>
  <summary>To create a folder</summary>

```python
new_folder = filemoon.create_fld(name='New Folder')
print(new_folder)
```

Optional parameter `parent_id` can be used to specify the parent folder ID.

```python
new_folder = filemoon.create_fld(name='New Folder', parent_id='PARENT_ID')
print(new_folder)
```

</details>

### Encoding Operations

<details>
  <summary>Get encoding list</summary>

```python
encoding_list = filemoon.en_list()
print(encoding_list)
```

</details>

<details>
  <summary>Get encoding status</summary>

```python
status = filemoon.en_status(file_code='FILE_CODE')
print(status)
```

</details>

<details>
  <summary>Restart encoding error files</summary>

```python
restart = filemoon.restart_en_error(file_code='FILE_CODE')
print(restart)
```

</details>

<details>
  <summary>Delete encoding error files</summary>

```python
delete = filemoon.delete_en_error(file_code='FILE_CODE')
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

### Remote Subtitle Management

<details>
  <summary>Add a remote subtitle</summary>

```python
subtitle = filemoon.r_sub(subnum='1', sub_url='https://example.com/subtitle.srt', sub_name='English Subtitles')
print(subtitle)
```

</details>

<details>
  <summary>Add remote subtitle in JSON format</summary>

```python
json_subtitle = filemoon.r_subjs(sub_js='{"subtitles": [{"url": "https://example.com/subtitle.srt", "label": "English"}]}')
print(json_subtitle)
```

</details>

<details>
  <summary>Add a remote poster</summary>

```python
poster = filemoon.r_post(r_post='https://example.com/poster.jpg')
print(poster)
```

</details>

<details>
  <summary>Add a remote logo</summary>

```python
logo = filemoon.r_logo(r_logo='https://example.com/logo.png')
print(logo)
```

</details>

### Server Management

<details>
  <summary>Get upload server URL</summary>

```python
upload_server = filemoon.up_server()
print(upload_server)
```

</details>

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues and pull requests to improve the codebase. All contributions are welcome!

## Author

Your Name - [BalaPriyan](https://github.com/BalaPriyan)

<hr style="border-top: 3px solid #000;">

