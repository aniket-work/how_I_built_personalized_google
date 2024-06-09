import json
import os


class URLFilter:
    def __init__(self, json_file):
        self.data = self.read_json(json_file)

    def read_json(self, json_file):
        with open(json_file, 'r') as file:
            return json.load(file)

    def get_active_urls(self):
        return self.data.get("Active", [])

    def write_active_urls_to_file(self, output_directory, output_filename="active_urls.json"):
        active_urls = self.get_active_urls()

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        output_path = os.path.join(output_directory, output_filename)

        with open(output_path, 'w') as outfile:
            json.dump({"Active": active_urls}, outfile, indent=4)


def main():
    json_file = 'web_crawler/web_crawler.json'

    url_filter = URLFilter(json_file)
    url_filter.write_active_urls_to_file(output_directory="indexer")


if __name__ == "__main__":
    main()
