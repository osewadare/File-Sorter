# -*- coding: cp1252 -*-
import wx,os,sys, shutil,wx.lib.agw.hyperlink as hl

id_choose = 1
id_music = 2
id_images = 3
id_videos = 4
id_documents = 5
id_apps = 6
id_clear = 7
id_about = 8
id_exit = 9


### Top Level Widget
class FileSorter(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300,405),style=wx.MINIMIZE_BOX
	| wx.SYSTEM_MENU | wx.CAPTION )

         ##Container
        panel = wx.Panel(self)

         #Styles

        self.font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Bradley Hand ITC')

        self.font2 = wx.Font(9, wx.SWISS, wx.NORMAL, wx.LIGHT, False, 'Calibiri Light')

        self.header_font = wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Georgia')

         #Widgets- Header

        self.header=wx.StaticText(panel, label='File Sorter', pos=(30, 25))

        self.header.SetForegroundColour('steel blue')

        self.header.SetFont(self.header_font)

        self.header2=wx.StaticText(panel, label='v.1.0 by GhostShield', pos=(130, 30))

        self.header2.SetFont(self.font)


        #Text

        static1 =wx.StaticBox(panel,-1,'Directory:',(7,73), size = (280,60))

        static2 =wx.StaticBox(panel,-1,'Mode',(7, 150 ), size = (280,35))

        static3=wx.StaticBox(panel,-1,'SorthFiles:',(7,207),size= (280, 65))

        static3=wx.StaticBox(panel,-1,'',(10,10),size= (280, 40))


        #TextCtrl

        self.folder_text = wx.TextCtrl(panel, -1,value='', size=(206, 20), pos=(70, 70))

        self.option =wx.RadioButton(panel,-1,' Sort Subfolders' , (66,150) , style = wx.RB_GROUP)

        self.option2=wx.RadioButton(panel,-1, 'Do not sort Subfolders' , (66,175))

        self.option2.SetValue(True)


        #Buttons

        choose = wx.Button(panel, id_choose, 'Choose Dir', size=(80, 25), pos=(82,100))
        self.Bind(wx.EVT_BUTTON, self.choose_folder,id=id_choose)

        choose.SetBackgroundColour('black')

        choose.SetForegroundColour('white')

        clear = wx.Button(panel, id_clear, 'New Task', size=(80, 25), pos=(178,100))
        self.Bind(wx.EVT_BUTTON, self.clear_folder,id=id_clear)

        self.about = wx.Button(panel, id_about, 'About', size=(80, 25), pos=(46, 320))
        self.Bind(wx.EVT_BUTTON, self.About, id=id_about)

        self.exit = wx.Button(panel, id_exit, 'Exit', size=(80, 25), pos=(175, 320))
        self.Bind(wx.EVT_BUTTON, self.OnCmdexit, id=id_exit)

        images = wx.Button(panel, id_images, 'Images', size=(60, 25), pos=(70,205))
        self.Bind(wx.EVT_BUTTON, self.images_sort,id=id_images)

        music = wx.Button(panel, id_music, 'Music', size=(60, 25), pos=(135,205))
        self.Bind(wx.EVT_BUTTON, self.music_sort,id=id_music)


        videos = wx.Button(panel, id_videos, 'Videos', size=(60, 25), pos=(200,205))
        self.Bind(wx.EVT_BUTTON, self.videos_sort,id=id_videos)

        documents = wx.Button(panel, id_documents, 'Docs', size=(60, 25), pos=(70,240))
        self.Bind(wx.EVT_BUTTON, self.documents_sort,id=id_documents)

        apps = wx.Button(panel, id_apps, 'Apps', size=(60, 25), pos=(135,240))
        self.Bind(wx.EVT_BUTTON, self.apps_sort,id=id_apps)

        #Hyperlink

        link1=hl.HyperLinkCtrl(panel,-1,'Like Ghost Shield', pos=(85,295),URL='http://www.facebook.com/ghostshieldvpn')
        link1.SetFont(self.font2)

        f = wx.Image('images/facebook.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(panel, -1, f, (187,290), (f.GetWidth(), f.GetHeight()))

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('                      Copyright © GhostShield 2014    ')

        # init tray icon
        self.Icon = wx.Icon('images/logo.ico', wx.BITMAP_TYPE_ICO)
        self.trayicon = wx.TaskBarIcon()
        self.traymsg = 'File Sorter'
        self.trayicon.SetIcon(self.Icon, self.traymsg)
        self.wndshown = True
        self.Bind(wx.EVT_ICONIZE, self.OnIconize)
        self.trayicon.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTrayIconClick)

        self.Centre()



    def OnIconize(self, event):
        """Called when user clicks minimize button."""
        self.Hide()
        self.wndshown = False

    def OnTrayIconClick(self, event):
        if self.wndshown:
            self.Hide()
            self.wndshown = False
        else:
            self.Iconize(False)
            self.Show(True)
            self.Raise()
            self.wndshown = True

    def choose_folder (self,event):
        dialog = wx.DirDialog(None, "Choose Folder to  Sort Files:" ,style=wx.DD_DEFAULT_STYLE |
        wx.DD_NEW_DIR_BUTTON)
        filesorter. Disable()
        if dialog.ShowModal() == wx.ID_OK:
            self.path = dialog.GetPath()
            filesorter.folder_text.SetValue(self.path)
        filesorter.Enable()
        dialog.Destroy()
        self.Raise()





    def clear_folder(self,event):
        self.folder_text.SetValue('')

    def About(self, event):

        description = """
Sort Files in Messy Folders
Email: info@ghostshield.tk
Mobile: +2348160613889
"""

        aboutinfo = wx.AboutDialogInfo()
        aboutinfo.SetName('File Sorter')
        aboutinfo.SetVersion('1.0')
        aboutinfo.SetDescription(description)
        aboutinfo.SetCopyright('(C) 2014 Ghost Shield')
        aboutinfo.SetWebSite('http://www.ghostshield.tk')
        aboutinfo.AddDeveloper('Osewa Damilare Joshua')
        wx.AboutBox(aboutinfo)

    def music_sort(self,event):
        path = filesorter.folder_text.GetValue()
        if len(path) > 1 :
                  if filesorter.option.GetValue() == True:
                     filesorta(path,(['.mp3'],['Music']))
                     filesorta(path,(['.amr'],['Music']))
                     filesorta(path,(['.wav'],['Music']))
                     filesorta(path,(['.ogg'],['Music']))
                     filesorta(path,(['.midi'],['Music']))
                     filesorta(path,(['.mid'],['Music']))
                     filesorta(path,(['.m4a'],['Music']))
                     filesorta(path,(['.wma'],['Music']))
                  elif filesorter.option2.GetValue() == True:
                     filesorta2(path,(['.mp3'],['Music']))
                     filesorta2(path,(['.amr'],['Music']))
                     filesorta2(path,(['.wav'],['Music']))
                     filesorta2(path,(['.ogg'],['Music']))
                     filesorta2(path,(['.midi'],['Music']))
                     filesorta2(path,(['.mid'],['Music']))
                     filesorta2(path,(['.m4a'],['Music']))
                     filesorta2(path,(['.wma'],['Music']))


                  d = wx.MessageDialog(self,'Music Files sorted : ' + path + '\Music ', 'Task Completed',wx.OK)
                  d.ShowModal()
        else:
            dlg = wx.MessageDialog(self,'Directory Not Selected', 'Error',wx.OK)
            dlg.ShowModal()


    def images_sort(self,event):
        path = filesorter.folder_text.GetValue()
        if len(path) > 1:
            if filesorter.option.GetValue() == True:
                filesorta(path,(['.jpg'],['Images']))
                filesorta(path,(['.png'],['Images']))
                filesorta(path,(['.jpeg'],['Images']))
                filesorta(path,(['.ico'],['Images']))
                filesorta(path,(['.gif'],['Images']))
                filesorta(path,(['.bmp'],['Images']))
            elif filesorter.option2.GetValue() == True:
                filesorta2(path,(['.jpg'],['Images']))
                filesorta2(path,(['.png'],['Images']))
                filesorta2(path,(['.jpeg'],['Images']))
                filesorta2(path,(['.ico'],['Images']))
                filesorta2(path,(['.gif'],['Images']))
                filesorta2(path,(['.bmp'],['Images']))

            d = wx.MessageDialog(self,'Image Files sorted : ' + path + '\Images', 'Task Completed',wx.OK)
            d.ShowModal()

        else :
            dlg = wx.MessageDialog(self,'Directory Not Selected', 'Error',wx.OK)
            dlg.ShowModal()

    def videos_sort(self,event):
        path = filesorter.folder_text.GetValue()
        if len(path) > 1:
            if filesorter.option.GetValue() == True:
                filesorta(path,(['.avi'],['Videos']))
                filesorta(path,(['.mp4'],['Videos']))
                filesorta(path,(['.flv'],['Videos']))
                filesorta(path,(['.swf'],['Videos']))
                filesorta(path,(['.mpeg'],['Videos']))
                filesorta(path,(['.wmv'],['Videos']))
                filesorta(path,(['.3gp'],['Videos']))
            elif filesorter.option2.GetValue() == True:
                filesorta2(path,(['.avi'],['Videos']))
                filesorta2(path,(['.mp4'],['Videos']))
                filesorta2(path,(['.flv'],['Videos']))
                filesorta2(path,(['.swf'],['Videos']))
                filesorta2(path,(['.mpeg'],['Videos']))
                filesorta2(path,(['.wmv'],['Videos']))
                filesorta2(path,(['.3gp'],['Videos']))

            d = wx.MessageDialog(self,'Video Files sorted : ' + path + '\Videos', 'Task Completed',wx.OK)
            d.ShowModal()

        else :
            dlg = wx.MessageDialog(self,'Directory Not Selected', 'Error',wx.OK)
            dlg.ShowModal()

    def documents_sort(self,event):
        path = filesorter.folder_text.GetValue()
        if len(path) > 1:
            if filesorter.option.GetValue() == True:
                filesorta(path,(['.docx'],['Documents']))
                filesorta(path,(['.doc'],['Documents']))
                filesorta(path,(['.pdf'],['Documents']))
                filesorta(path,(['.pptx'],['Documents']))
                filesorta(path,(['.odb'],['Documents']))
                filesorta(path,(['.txt'],['Documents']))
            elif filesorter.option2.GetValue() == True:
                filesorta2(path,(['.docx'],['Documents']))
                filesorta2(path,(['.doc'],['Documents']))
                filesorta2(path,(['.pdf'],['Documents']))
                filesorta2(path,(['.pptx'],['Documents']))
                filesorta2(path,(['.odb'],['Documents']))
                filesorta2(path,(['.txt'],['Documents']))

            d = wx.MessageDialog(self,'Document Files sorted : ' + path + '\Documents', 'Task Completed',wx.OK)
            d.ShowModal()
        else :
            dlg = wx.MessageDialog(self,'Directory Not Selected', 'Error',wx.OK)
            dlg.ShowModal()

    def apps_sort(self,event):
        path = filesorter.folder_text.GetValue()
        if len(path) > 1:
            if filesorter.option.GetValue() == True:
                filesorta(path,(['.exe'],['Applications']))
                filesorta(path,(['.apk'],['Applications']))
                filesorta(path,(['.jar'],['Applications']))
            elif filesorter.option2.GetValue() == True:
                filesorta2(path,(['.exe'],['Applications']))
                filesorta2(path,(['.apk'],['Applications']))
                filesorta2(path,(['.jar'],['Applications']))
            d = wx.MessageDialog(self,'Appliication Files sorted : ' + path + '\Applications', 'Task Completed',wx.OK)
            d.ShowModal()
        else :
            dlg = wx.MessageDialog(self,'Directory Not Selected', 'Error',wx.OK)
            dlg.ShowModal()

    def OnCmdexit(self,event):
            self.trayicon.RemoveIcon()
            sys.exit(0)

def filesorta(path, folfil, recursion=0, xfil=''):
        global err
       # filesorter.status_text.SetLabel(" Sorting directory.. "+ path+xfil)
        d=os.listdir(path+xfil)
        foldn=folfil[1]
        filex=folfil[0]
        for i in d:
            if os.path.isdir(path+'/'+i) and i not in foldn  :
                #filesorter.status_text.SetLabel(" Folder detected. Proceeding to sort folder..  ")
                filesorta(path, (filex, foldn), recursion+1, xfil+'/'+i)
                continue
            if '.'+i.partition('.')[2] in filex:
                aa=foldn[filex.index('.'+i.partition('.')[2])]
                try: shutil.move(path+xfil+'/'+i, path+'/'+aa+'/'+i)
                except IOError:
                    try: os.mkdir(path+'/'+aa)
                    except WindowsError as (errno, strerror):
                        err+=1
                        #print "WindowsError", errno, strerror
                    shutil.move(path+xfil+'/'+i, path+'/'+aa+'/'+i)


def filesorta2(path, folfil, recursion=0, xfil=''):
        global err
        #filesorter.status_text.SetLabel(" Sorting directory.. "+ path+xfil)
        d=os.listdir(path+xfil)
        foldn=folfil[1]
        filex=folfil[0]
        for i in d:
            if '.'+i.partition('.')[2] in filex:
                aa=foldn[filex.index('.'+i.partition('.')[2])]
                try: shutil.move(path+xfil+'/'+i, path+'/'+aa+'/'+i)
                except IOError:
                    try: os.mkdir(path+'/'+aa)
                    except WindowsError as (errno, strerror):
                        err+=1
                        #print "WindowsError", errno, strerror
                    shutil.move(path+xfil+'/'+i, path+'/'+aa+'/'+i)






app = wx.App()
filesorter = FileSorter(None, -1, 'File Sorter')
filesorter.Show(True)
app.MainLoop()















