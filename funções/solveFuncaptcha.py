from anticaptchaofficial.funcaptchaproxyless import *
def solveFuncaptcha():

    solver = funcaptchaProxyless()
    solver.set_verbose(1)
    solver.set_key("key anticaptcha")
    solver.set_website_url("https://octocaptcha.com") #link do site
    solver.set_website_key("69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC") #key do site
    solver.set_soft_id(0)

    token = solver.solve_and_return_solution()
    if token != 0:
        print(token) #imprime resultado do captcha e retorna
        return token
    else:
        print("task finished with error "+solver.error_code)

result = solveFuncaptcha()
