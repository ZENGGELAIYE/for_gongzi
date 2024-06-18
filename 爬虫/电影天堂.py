# import requests
# url = 'https://dytt89.com/'
# headers = {
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
# }
# resp = requests.get(url = url,verify=False,headers=headers)
# resp.encoding = 'gbk'
# print(resp.text)

import asyncio
from pyppeteer import launch
async def main():
    # 启动浏览器
    browser = await launch()
    # 打开新页面
    page = await browser.newPage()
    # 导航到指定的网页
    await page.goto('www.baidu.com')
    # 获取页面的 HTML 内容
    html_content = await page.content()
    print(html_content)
    return html_content
    # 关闭浏览器SS
    # await browser.close()

# 运行主函数
asyncio.get_event_loop().run_until_complete(main())
