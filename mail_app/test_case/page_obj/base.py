


# 基本层
class Base(object):

    def __init__(self,driver,base_url="http://mail.163.com"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def _open(self,url):
        url_ = self.base_url + url # = http://www.126.com/index.html
        #print(url_)
        self.driver.get(url_)
        assert self.driver.current_url == url_ ,'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    # *loc参数个数不是固定 *loc = (By.ID,"kw")
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def iframe(self,iframeid):
        return self.driver.switch_to.frame(iframeid)

    def iframe_out(self):
        return self.driver.switch_to.default_content()

    def script(self,src):
        return self.driver.execute_script(src)
