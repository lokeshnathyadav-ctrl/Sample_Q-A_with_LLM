from huggingface_hub import HfApi
import os
os.environ['HF_TOKEN'] = userdata.get('HF_TOKEN')
hf_api_key = userdata.get('HF_TOKEN')
api = HfApi(token=hf_api_key)
repo_id="Lokeshnathy/Sample-q-a",
repo_type="space"
api.upload_folder(
    folder_path="content/drive/MyDrive/sample_q&a/deployment",
    repo_id=repo_id,
    repo_type=repo_type
)
