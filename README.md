# dicom_nc_gui
DICOM image copier for preparing images for use in the Nextcloud DICOM Viewer

Python tkinter application that allows you to copy DICOM files and prepares them for use in the Nextcloud DICOM Viewer.
Provide a source directory, destination directory, and (optionally) a comma separated list of extensions to ignore, and
the app will copy the files to the destination directory and rename them so that they have an extension of ".dcm" if
they don't already have that extension.

There is a Preview button that shows what will happen if the Submit button is pressed. This allows you to fine-tune the
extensions to exclude.

The Nextcloud DICOM Viewer expects all DICOM images to be in the same directory and the extensions to be ".dcm". Most 
medical discs have the images spread across multiple folders, some discs have DICOM images with no extensions, and many 
of the files spread acroos the folders have the same name (e.g. view0001.dcm in different folders). So simply copying
the files to one directory will not work.

This program will rename the files it copies based on the directory path they were in. For instance, if a file's source
path and filename is "./p334499/s433222/view0001.dcm", the file will be copied to the destination directory and also
renamed to "p334499-s433222-view0001.dcm". By including the path and changing the path separator to a dash, each file
will be uniquely named when copied to the destination folder.

![image](https://user-images.githubusercontent.com/5542950/181347953-036cc0e5-dc1d-4d96-90cc-bcd66b651ecf.png)
