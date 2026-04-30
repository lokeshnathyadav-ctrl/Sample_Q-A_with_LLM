from huggingface_hub import HfApi
import os
#os.environ['HF_TOKEN'] = userdata.get('HF_TOKEN')
hf_api_key = os.getenv('HF_TOKEN')
api = HfApi(token=hf_api_key)

api.upload_folder(
    folder_path = "content/drive/MyDrive/sample_qa/deployment",
    repo_id = "Lokeshnathy/sample-q-a",
    repo_type = "space"
)
