# Image-Captcha-Solver

Solves ~20000 Kinds of image captchas, including old reCAPTCHA, Google, Solve Media etc. Basically every image captcha.
Image size should be <0.1mb 

result example:
<code>
{"solution":"338712"}
</code>

You can also load just the result like this:
###

import json 
data=json.loads(response.text) 
print(data['solution']) 

Script works through Rapidapi and uses this API: https://rapidapi.com/DaddyApi/api/image-captcha-solver-daddy/

You will your api key, in order to solve. There is a free tier.
