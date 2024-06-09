import json
import os


class URLFilter:
    """
    A class to filter URLs from a JSON file and write active URLs to another JSON file.

    Attributes:
    json_file (str): The path to the input JSON file.
    data (dict): The JSON data loaded from the input file.
    """

    def __init__(self, json_file):
        """
        Initializes the URLFilter with the provided JSON file.

        Args:
        json_file (str): The path to the input JSON file.
        """
        self.data = self.read_json(json_file)

    def read_json(self, json_file):
        """
        Reads JSON data from the input file.

        Args:
        json_file (str): The path to the input JSON file.

        Returns:
        dict: The JSON data loaded from the file.
        """
        with open(json_file, 'r') as file:
            return json.load(file)

    def get_active_urls(self):
        """
        Retrieves active URLs from the loaded JSON data.

        Returns:
        list: A list of active URLs.
        """
        return self.data.get("Active", [])

    def write_active_urls_to_file(self, output_directory, output_filename="active_urls.json"):
        """
        Writes active URLs to a JSON file.

        Args:
        output_directory (str): The directory where the output file will be saved.
        output_filename (str): The name of the output JSON file. Defaults to "active_urls.json".
        """
        active_urls = self.get_active_urls()

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        output_path = os.path.join(output_directory, output_filename)

        with open(output_path, 'w') as outfile:
            json.dump({"Active": active_urls}, outfile, indent=4)


def main():
    """
    Main function to execute the URL filtering and writing process.
    """
    json_file = 'web_crawler/web_crawler.json'

    url_filter = URLFilter(json_file)
    url_filter.write_active_urls_to_file(output_directory="indexer")


if __name__ == "__main__":
    main()
