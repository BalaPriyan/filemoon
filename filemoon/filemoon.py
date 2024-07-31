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
        self, per_page: Optional[int] = None, page: Optional[int] = None
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
        self, per_page: Optional[int] = None, page: Optional[int] = None
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
    ) -> dict:
        """
        Upload files using direct links

        Args:
            direct_link (str): URL to upload

        Returns:
            dict: response
        """
        url = f"{self.base_url}remote/add?key={self.api_key}&url={direct_link}"
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




