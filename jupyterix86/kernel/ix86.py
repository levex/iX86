from ipykernel.kernelbase import Kernel
import subprocess
import random
import os
import string

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

class KerneliX86(Kernel):
    implementation = 'iX86'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "iX86 - x86 Assembly programming in Jupyter"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            rname = randomword(10)
            filename = '/tmp/jix6-' + rname + '.S'
            #print(os.path.join(os.path.dirname(__file__), '../support/base_Darwin.S'))
            subprocess.run(['cp', os.path.join(os.path.dirname(__file__), '../support/base_Darwin.S'), filename])
            file = open(filename, "r+")
            cts = file.read()
            cts = cts.replace('##__CODE__HERE__##', code)
            file.seek(0)
            file.write(cts)
            file.truncate()
            file.close()
            result = subprocess.run([os.path.join(os.path.dirname(__file__), '../support/base_Darwin.sh'), filename, rname], stdout=subprocess.PIPE)
            subprocess.run(['rm', filename])
            stream_content = {'name': 'stdout', 'text': str(result.stdout)}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=KerneliX86)
