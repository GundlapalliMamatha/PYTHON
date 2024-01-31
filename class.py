class services:
    def _init_(self,appleservice,samsungservice,lgservice):
        self.a_service=appleservice
        self.s_service=samsungservice
        print(self.a_service,self.s_service)
services("macbook")