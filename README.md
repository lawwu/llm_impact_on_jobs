# LLM Impact on Jobs

Code to use llama2-13b-chat locally to assess the impact of LLMs on jobs. I'm using ONET's list of occupations, which has 1,016 unique titles.  

## Setup
Create virutal env
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# install llama-cpp-python so it works with Apple Silicon
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python
```
