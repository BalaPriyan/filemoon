import requests
from typing import Optional

class FileMoon:
    def __init__(self, api_key: str, base_url: str = 'https://filemoonapi.com/api/', player_url: str = 'https://filemoonapi.com/e/'):
        """
        init

        Args:
            api_key (str): api key from filemoon
            base_url (str, optional): base api url. Defaults to "https://filemoonapi.com/api/".
        """
        self.api_key = api_key
        self.base_url = base_url

    def _req(self, url: str) -> dict:
        """requests to api

        Args:
            url (str): api url

        Return:
            (dict): output dict from requests url"""
        try:
            r = requests.get(url)
            response = r.json()
            if response.get("msg") == "Wrong Auth":
                raise Exception("Invalid API key, please check your API key")
            else:
                return response
        except requests.ConnectionError as e:
            raise Exception(e)

    def info(self) -> dict:
        """
        Get basic info of your account

        Returns:
            dict: response
        """
        url = f"{self.base_url}account/info?key={self.api_key}"
        return self._req(url)

    def stats(self, last: Optional[str] = None) -> dict:
        """
        Get reports of your account (default last 7 days)

        Args:
            last (Optional[str], optional): Last x days report. Defaults to None.
        Returns:
            dict: response
        """
        url = f"{self.base_url}account/stats?key={self.api_key}"
        if last is not None:
            url += f"&last={last}"
        return self._req(url)

    def dmca(self, last: Optional[str] = None) -> dict:
        """
        Get DMCA reported files list (500 results per page)

        Args:
            last (Optional[str], optional): Last x file got DMCA. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}files/dmca?key={self.api_key}"
        if last is not None:
            url += f"&last={last}"
        return self._req(url)

    def deleted(self, last: Optional[str] = None) -> dict:
        """
        Get deleted files list (500 results per page)

        Args:
            last (Optional[str], optional): Last x files got deleted. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}files/deleted?key={self.api_key}"
        if last is not None:
            url += f"&last={last}"
        return self._req(url)

    def remote_upload(self, direct_link: str, fld_id: Optional[str] = None) -> dict:
        """
        Upload files using direct links

        Args:
            direct_link (str): URL to upload
            fld_id (Optional[str]): Folder ID to upload to. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}remote/add?key={self.api_key}&url={direct_link}"
        if fld_id is not None:
            url += f"&fld_id={fld_id}"
        return self._req(url)

    def remove_rup(self, file_code: str) -> dict:
        """
        To remove remote Upload

        Args:
            file_code (str): file code to remove the file from remote upload

        Returns:
            dict: response
        """
        url = f"{self.base_url}remote/remove?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def rup_status(self, file_code: str) -> dict:
        """
        To check remote Upload status

        Args:
            file_code (str): to check upload status

        Returns:
            dict: response
        """
        url = f"{self.base_url}remote/status?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def f_info(self, file_code: str) -> dict:
        """
        To get file info

        Args:
            file_code (str): to get file info

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/info?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def f_list(self,
                  fld_id: Optional[str] = None,
                  name: Optional[str] = None,
                  created: Optional[str] = None,
                  public: Optional[str] = None,
                  per_page: Optional[str] = None,
                  page: Optional[str] = None) -> dict:
        """
        To List A File 

        Args:
            fld_id (Optional[str]): Folder ID to list files from. Defaults to None.
            name (Optional[str]): To Fetch A File By Name. Defaults to None.
            created (Optional[str]): To fetch by created date. Defaults to None.
            public (Optional[str]): To fetch by public media. Defaults to None.
            per_page (Optional[str]): To fetch by per page. Defaults to None.
            page (Optional[str]): To fetch by page. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/list?key={self.api_key}"
        if fld_id is not None:
            url += f"&fld_id={fld_id}"
        if name is not None:
            url += f"&name={name}"
        if created is not None:
            url += f"&created={created}"
        if public is not None:
            url += f"&public={public}"
        if per_page is not None:
            url += f"&per_page={per_page}"
        if page is not None:
            url += f"&page={page}"
        return self._req(url)

    def clone_f(self, file_code: str, fld_id: Optional[str] = None) -> dict:
        """
        To clone file

        Args:
            file_code (str): to clone file
            fld_id (Optional[str]): To clone to specific folder. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/clone?key={self.api_key}&file_code={file_code}"
        if fld_id is not None:
            url += f"&fld_id={fld_id}"
        return self._req(url)

    def fld_list(self, fld_id: Optional[str] = None) -> dict:
        """
        To get folder list

        Args:
            fld_id (Optional[str]): Folder ID to get list from. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}folder/list?key={self.api_key}"
        if fld_id is not None:
            url += f"&fld_id={fld_id}"
        return self._req(url)

    def create_fld(self, name: str, parent_id: Optional[str] = None) -> dict:
        """
        To create folder 

        Args:
            name (str): Folder name
            parent_id (Optional[str]): Parent folder ID. Defaults to None.

        Returns:
            dict: response
        """
        if name is None:
            raise ValueError("The 'name' parameter is required.")
        url = f"{self.base_url}folder/create?key={self.api_key}&name={name}"
        if parent_id is not None:
            url += f"&parent_id={parent_id}"
        return self._req(url)

    def en_list(self) -> dict:
        """
        Get encoding list

        Returns:
            dict: response
        """
        url = f"{self.base_url}encoding/list?key={self.api_key}"
        return self._req(url)

    def en_status(self, file_code: str) -> dict:
        """
        Get encoding file list

        Args:
            file_code (str): file code check status

        Returns:
            dict: response
        """
        url = f"{self.base_url}encoding/status?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def restart_en_error(self, file_code: str) -> dict:
        """
        To restart encoding error files

        Args:
            file_code (str): to restart the encoding error files

        Returns:
            dict: response
        """
        url = f"{self.base_url}encoding/restart?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def delete_en_error(self, file_code: str) -> dict:
        """
        To delete encode error files

        Args:
            file_code (str): to delete the encode error files

        Returns:
            dict: response
        """
        url = f"{self.base_url}encoding/delete?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def thumb(self, file_code: str) -> dict:
        """
        To get thumbnail image URL

        Args:
            file_code (str): to get thumbnail URL from specific file

        Returns:
            dict: response
        """
        url = f"{self.base_url}images/thumb?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def splash(self, file_code: str) -> dict:
        """
        To get splash image from specific file

        Args:
            file_code (str): to get splash image from specific file

        Returns:
            dict: response
        """
        url = f"{self.base_url}images/splash?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def vid_preview(self, file_code: str) -> dict:
        """
        To get video preview of specific file

        Args:
            file_code (str): to get video preview of specific file

        Returns:
            dict: response
        """
        url = f"{self.base_url}images/preview?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def r_sub(self, subnum: str, sub_url: str, sub_name: str) -> dict:
        """
        to add remote subtitle

        Args:
           subnum(str): subtitle number
           sub_url(str): subtitle remote url
           sub_name(str): subtitle name
        Returns:
            dict: response
        """
        url = f"{self.player_url}file_code?c{subnum}_file={sub_url}&c{subnum}_label={sub_name}"
        return self._req(url)
