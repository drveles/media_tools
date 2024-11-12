import os


class ProcessMedia:
    def __init__(self, path):
        self._source_path = self._create_full_source_path(path)
        self._output_path = self._create_full_output_path(self._source_path)

    def _create_full_source_path(self, path: str) -> str:
        full_path = os.path.join(path)
        if not os.path.exists(full_path):
            raise FileNotFoundError
        return full_path

    def _create_full_output_path(self, full_path: str) -> str:
        output_dir = "results"
        os.makedirs(output_dir, exist_ok=True)

        file_name = os.path.basename(full_path)
        file_name_without_ext = os.path.splitext(file_name)[0]

        output_path = os.path.join(output_dir, f"{file_name_without_ext}.mp3")
        return output_path
