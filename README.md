# dicom_nc_gui
DICOM image copier for preparing images for use in the Nextcloud DICOM Viewer

Python tkinter application that allows you to copy DICOM files and prepares them for use in the Nextcloud DICOM Viewer.
Provide a source directory, destination directory, and (optionally) a comma separated list of extensions to ignore, and
the app will copy the files to the destination directory and rename them so that they have an extension of ".dcm" if
they don't already have that extension.

There is a Preview button that shows what will happen if the Submit button is pressed. This allows you to fine-tune the
extensions to exclude.

![image](https://user-images.githubusercontent.com/5542950/181347953-036cc0e5-dc1d-4d96-90cc-bcd66b651ecf.png)
