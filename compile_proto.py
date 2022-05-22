from pathlib import Path
import subprocess

protoc = 'protoc'
source_dir = Path('proto')
output_dir = 'pb2'

for file in source_dir.glob('**/*.proto'):
    subprocess.run([protoc, '--proto_path=proto', '--python_out={}'.format(output_dir), str(file)])
