import requests
import re
import sys
from typing import Optional

class FileMoon:
  def __init__(self, api_key:str, base_url:'https://filemoonapi.com/api/'):
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
            if response["msg"] == "Wrong Auth":
                Exception("Invalid API key, please check your API key")
            else:
                return response
        except ConnectionError as e:
            Exception(e)


    def account_info(self) -> dict:
        """
        Get basic info of your account

        Returns:
            dict: response
        """
        url = f"{self.base_url}account/info?key={self.api_key}"
        return self._req(url)

    def account_stats(
        self,
        last: Optional[str] = None,
    ) -> dict:
        """
        Get reports of your account (default last 7 days)

        Args:
            last (Optional[str], optional): Last x days report. Defaults to None.
        Returns:
            dict: response
        """
        url = f"{self.base_url}account/stats?key={self.api_key}"
        if last != None:
            url += f"&last={last}"
        return self._req(url)


    def dmca_list(
        self, last: Optional[str] = None,
    ) -> dict:
        """
        Get DMCA reported files list (500 results per page)

        Args:
            last (Optional[str], optional): Last x file got dmca. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}files/dmca?key={self.api_key}"
        if last != None:
            url += f"&last={last}"
        return self._req(url)

    def deleted_list(
        self, last: Optional[str] = None,
    ) -> dict:
        """
        Get DMCA reported files list (500 results per page)

        Args:
            last (Optional[str], optional): Last x files got deleted. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}files/deleted?key={self.api_key}"
        if last != None:
            url += f"&last={last}"
        return self._req(url)

    def remote_upload(
        self,
        direct_link: str,
        fld_id: Optional[str] = None
    ) -> dict:
        """
        Upload files using direct links

        Args:
            direct_link (str): URL to upload

        Returns:
            dict: response
        """
        url = f"{self.base_url}remote/add?key={self.api_key}&url={direct_link}"
        if fld_id != None:
          url += f"&fld_id={folder_id}"
        return self._req(url)


    def reremote_upload(
        self,
        file_code: str,
    ) -> dict:
        """
        To remove remote Upload

        Args:
            file_code (str): file code to remove the file from remote upload

        Returns:
            dict: response
        """
        url = f"{self.base_url}remote/remove?key={self.api_key}&file_code={file_code=}"
        return self._req(url)


    def remote_upload_status(
        self,
        file_code: str,
    ) -> dict:
        """
        To check remote Upload status

        Args:
            file_code (str): to check upload status

        Returns:
            dict: response
        """
        url = f"{self.base_url}remote/status?key={self.api_key}&file_code={file_code=}"
        return self._req(url)


    def file_info(
        self,
        file_code: str,
    ) -> dict:
        """
        To get file info

        Args:
            file_code (str): to get file info

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/info?key{self.api_key}&file_code={file_code=}"
        return self._req(url)

    def file_list(
        self,
        fld_id: Optional[str] = None,
        name: Optional[str] = None,
        created: Optional[str] = None,
        public: Optional[str] = None,
        per_page: Optional[str] = None,
        page: Optional[str] = None,
    ) -> dict:
        """
        To List A File 

        Args:
        name (str):To Fetch A File By Name
        created(str): to fetch by created date
        public(str):to fetch by public media 
        per_page(str): to fetch by per page
        page(str): to fetch by page
        fld_id: to fetch from folder
        
        
            

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/list?key={self.api_key}"
        if fld_id != None:
          url += f"&fld_id={folder_id}"
        if page != None:
          url += f"&page={page}"
        if per_page += None:
          url += f"&per_page={per_page}"
        if public += None:
          url += f"&public={public}"
        if created != None:
          url += f"&created={created}"
        if name != None:
          url += f"&name={name}"
        return self._req(url)


    def clone_file(
        self,
        file_code: str,
        fld_id: Optional[str] = None,
    ) -> dict:
        """
        To clone file

        Args:
            file_code (str): to clone file
            fld_id(str): To Clone to specific folder

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/clone?key={self.api_key}&file_code={file_code=}"
        if fld_id = None:
          url += f"&fld_id={fld_id}"
        return self._req(url)

    def folder_list(
        self,
        fld_id: Optional[str] = None,
    ) -> dict:
        """
        To get folder list

        Args:
            fld_id (str): to get folder list

        Returns:
            dict: response
        """
        url = f"{self.base_url}folder/list?key={self.api_key}"
        if fld_id != None:
          url = f"&fld_id={fld_id}"
        return self._req(url)

    def create_folder(
        self,
        parent_id: Optional[str] = None,
        name: str,
    ) -> dict:
        """
        To create folder 

        Args:
            parent_id (str): folder parent ID
            name(str) folder name

        Returns:
            dict: response
        """
        if name is None:
          raise ValueError("The 'name' parameter is required.")
        url = f"{self.base_url}folder/create?key={self.api_key}"
        if parent_id != None:
          url += f"&parent_id={parent_id}"
        url += f"&name={name}"
        return self._req(url)

    def encode_list(self) -> dict:
        """
        Get encoding list

        Returns:
            dict: response
        """
        url = f"{self.base_url}encoding/list?key=={self.api_key}"
        return self._req(url)

    def encode_status(self,
                     file_code: str,
                     ) -> dict:
        """
        Get encoding file list

        Args:
           file_code(str): file code check status

        Returns:
            dict: response
        """
        url = f"{self.base_url}encoding/status?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def restart_encode_error(self,
                             file_code: str,) -> dict:
        """
        To Restart encoding error files
        Args:
            file_code(str): to restart The Encoding error files

        Returns:
            dict: response
        """
        url = f"{self.base_url}encoding/restart?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def delete_encode_error(self, file_code: str,) -> dict:
        """
        To Delete Encode Error Files

        Args:
           file_code(str): To Delete The Encode Error files

        Returns:
            dict: response
        """
        url = f"{self.base_url}encoding/delete?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def thumb(self, file_code: str,) -> dict:
        """
        to get Thumbnail image url

        Args:
          file_code(str): to get thumb url from specific file

        Returns:
            dict: response
        """
        url = f"{self.base_url}images/thumb?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def splash(self, file_code: str,) -> dict:
        """
        To Get Splash From specific File 

        Args:
            file_code (str): to get splash from specific file

        Returns:
            dict: response
        """
        url = f"{self.base_url}images/splash?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def vid_preview(self,file_code: str,) -> dict:
        """
        To Get video preview of specific file

        Args:
            To Get Video Preview Of Specific Video File

        Returns:
            dict: response
        """
        url = f"{self.base_url}images/preview?key={self.api_key}&file_code={file_code}"
        return self._req(url)
