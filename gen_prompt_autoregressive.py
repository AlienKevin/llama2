from hazel_samples import samples

prompt = [
    "USER: ",
    "ASSISTANT: ",
]

import re
suffix_re = re.compile("\?\?(?s:.+)")
test_re = re.compile("test (?s:.+)")

for (sketch, program) in samples:
    print(prompt[0] + suffix_re.sub("", sketch).strip())
    print(prompt[1] + test_re.sub("", program).strip())
    print()
