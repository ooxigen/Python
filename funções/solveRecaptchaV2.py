from anticaptchaofficial.recaptchav2proxyless import *
def solveRecaptchaV2():

    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("key anticaptcha")
    solver.set_website_url("https://2captcha.com/demo/recaptcha-v2") #link do site
    solver.set_website_key("6LfD3PIbAAAAAJs_eEHvoOl75_83eXSqpPSRFJ_u") #key do site
    solver.set_soft_id(0)

    token = solver.solve_and_return_solution()
    if token != 0:
        print(token) #imprime resultado do captcha e retorna
        return token
    else:
        print("task finished with error "+solver.error_code)

result = solveRecaptchaV2()
