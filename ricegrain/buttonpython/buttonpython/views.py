import subprocess
from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage
from package.extFile import ratio


'''cmd='python image.py'
p=subprocess.Popen(cmd,shell=True)
out,err=p.communicate()
print(out)'''
def button(request):

    return render(request,'home.html')

'''def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})'''

def external(request):
    try:
        #inp= request.POST.get('param')
        image=request.FILES['image']
        print("image is ",image)
        fs=FileSystemStorage()
        filename=fs.save(image.name,image)
        fileurl=fs.open(filename)
        templateurl=fs.url(filename)
        print("file raw url",filename)
        print("file full url", fileurl)
        print("template url",templateurl)
        #out= run([sys.executable,'E:/ricegrain/test.py',inp],shell=False,stdout=PIPE)
        image= run([sys.executable,'E:/ricegrain/image.py',str(fileurl),str(filename)],shell=False,stdout=PIPE)
        #print(out)
        #out=subprocess.check_output([sys.executable,"image.py","34"])
        #print(image.get_classificaton(avg_ar))
        k=ratio()
        print(k)
        #print(image.stdout)
        #return render(request,'home.html',{'raw_url':templateurl,'edit_url':image.stdout})
    except Exception:
        return render(request,'home.html',{'data':k})

    return render(request,'home.html',{'data':k})

