# Image-Captcha-Solver

Solve simple image captchas, image size should be <0.1mb 

Solves words as well as digits. The simpler the captcha, the more accurate it is.

result example:

{"solution":"338712"}


You can also load just the result like this:
###
<code>
import json 
data=json.loads(response.text) 
print(data['solution']) 
</code>
