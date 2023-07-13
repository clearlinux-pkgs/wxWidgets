#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
%define keepstatic 1
Name     : wxWidgets
Version  : 3.2.2.1
Release  : 31
URL      : https://github.com/wxWidgets/wxWidgets/releases/download/v3.2.2.1/wxWidgets-3.2.2.1.tar.bz2
Source0  : https://github.com/wxWidgets/wxWidgets/releases/download/v3.2.2.1/wxWidgets-3.2.2.1.tar.bz2
Summary  : Posix compatible interface to libpcre2-8
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 GPL-2.0 HPND LGPL-2.0 Libpng MIT TCL Zlib libtiff
Requires: wxWidgets-bin = %{version}-%{release}
Requires: wxWidgets-data = %{version}-%{release}
Requires: wxWidgets-lib = %{version}-%{release}
Requires: wxWidgets-license = %{version}-%{release}
Requires: wxWidgets-locales = %{version}-%{release}
BuildRequires : cairo-dev
BuildRequires : glu-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gspell-1)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-player-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libmspack)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : pkgconfig(pangoxft)
BuildRequires : pkgconfig(sdl)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(xtst)
BuildRequires : tiff-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
------------------------------------------------------------------
PCRE2 is a re-working of the original PCRE1 library to provide an entirely new
API. Since its initial release in 2015, there has been further development of
the code and it now differs from PCRE1 in more than just the API. There are new
features, and the internals have been improved. The original PCRE1 library is
now obsolete and should not be used in new projects. The latest release of
PCRE2 is available in three alternative formats from:

%package bin
Summary: bin components for the wxWidgets package.
Group: Binaries
Requires: wxWidgets-data = %{version}-%{release}
Requires: wxWidgets-license = %{version}-%{release}

%description bin
bin components for the wxWidgets package.


%package data
Summary: data components for the wxWidgets package.
Group: Data

%description data
data components for the wxWidgets package.


%package dev
Summary: dev components for the wxWidgets package.
Group: Development
Requires: wxWidgets-lib = %{version}-%{release}
Requires: wxWidgets-bin = %{version}-%{release}
Requires: wxWidgets-data = %{version}-%{release}
Provides: wxWidgets-devel = %{version}-%{release}
Requires: wxWidgets = %{version}-%{release}

%description dev
dev components for the wxWidgets package.


%package lib
Summary: lib components for the wxWidgets package.
Group: Libraries
Requires: wxWidgets-data = %{version}-%{release}
Requires: wxWidgets-license = %{version}-%{release}

%description lib
lib components for the wxWidgets package.


%package license
Summary: license components for the wxWidgets package.
Group: Default

%description license
license components for the wxWidgets package.


%package locales
Summary: locales components for the wxWidgets package.
Group: Default

%description locales
locales components for the wxWidgets package.


%prep
%setup -q -n wxWidgets-3.2.2.1
cd %{_builddir}/wxWidgets-3.2.2.1
pushd ..
cp -a wxWidgets-3.2.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689275824
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%autogen  --with-gtk=3 \
--enable-cxx11 \
--enable-debug_gdb \
--enable-intl \
--enable-notebook \
--enable-compat28
make  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%autogen  --with-gtk=3 \
--enable-cxx11 \
--enable-debug_gdb \
--enable-intl \
--enable-notebook \
--enable-compat28
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1689275824
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wxWidgets
cp %{_builddir}/wxWidgets-%{version}/3rdparty/catch/LICENSE.txt %{buildroot}/usr/share/package-licenses/wxWidgets/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/wxWidgets-%{version}/3rdparty/nanosvg/LICENSE.txt %{buildroot}/usr/share/package-licenses/wxWidgets/f4f94babc436555d2f5992e29aacc47433fbadb4 || :
cp %{_builddir}/wxWidgets-%{version}/3rdparty/pcre/LICENCE %{buildroot}/usr/share/package-licenses/wxWidgets/3005b2c68faac406829c8ea56376ddcb1ed0eabb || :
cp %{_builddir}/wxWidgets-%{version}/3rdparty/pcre/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/wxWidgets/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/wxWidgets-%{version}/build/cmake/modules/cotire_test/license %{buildroot}/usr/share/package-licenses/wxWidgets/ece76272e705e27f0c76531aac6dd0b10820bc10 || :
cp %{_builddir}/wxWidgets-%{version}/docs/gpl.txt %{buildroot}/usr/share/package-licenses/wxWidgets/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/wxWidgets-%{version}/docs/wine/COPYING.LIB %{buildroot}/usr/share/package-licenses/wxWidgets/ec2350cf4fe9c4f97c3ee5c9046d0396672c365a || :
cp %{_builddir}/wxWidgets-%{version}/src/expat/expat/COPYING %{buildroot}/usr/share/package-licenses/wxWidgets/8623dd26727a708a49dbe6a52edb1d931d70816d || :
cp %{_builddir}/wxWidgets-%{version}/src/motif/mdi/COPYRIGHT %{buildroot}/usr/share/package-licenses/wxWidgets/3f65d8e23a75d7c0a9a7b7092c9249e4f8cd2db4 || :
cp %{_builddir}/wxWidgets-%{version}/src/motif/xmcombo/copying.txt %{buildroot}/usr/share/package-licenses/wxWidgets/17e3b0eea99abffe6ac71e65627413236e0b117a || :
cp %{_builddir}/wxWidgets-%{version}/src/png/LICENSE %{buildroot}/usr/share/package-licenses/wxWidgets/fc3951ba26fe1914759f605696a1d23e3b41766f || :
cp %{_builddir}/wxWidgets-%{version}/src/regex/COPYRIGHT %{buildroot}/usr/share/package-licenses/wxWidgets/9a5a0d7c8ffa82a9489acbb7f0d6947a2b1bc27f || :
cp %{_builddir}/wxWidgets-%{version}/src/stc/scintilla/License.txt %{buildroot}/usr/share/package-licenses/wxWidgets/9da27f7b263edb706105ccd68880474013b11bca || :
cp %{_builddir}/wxWidgets-%{version}/src/tiff/COPYRIGHT %{buildroot}/usr/share/package-licenses/wxWidgets/a2f64f2a85f5fd34bda8eb713c3aad008adbb589 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang wxstd-3.2
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/wx/config/gtk3-unicode-3.2

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/wxrc-3.2
/usr/bin/wx-config
/usr/bin/wxrc
/usr/bin/wxrc-3.2

%files data
%defattr(-,root,root,-)
/usr/share/bakefile/presets/wx.bkl
/usr/share/bakefile/presets/wx_presets.py
/usr/share/bakefile/presets/wx_unix.bkl
/usr/share/bakefile/presets/wx_win32.bkl
/usr/share/bakefile/presets/wx_xrc.bkl

%files dev
%defattr(-,root,root,-)
/usr/include/wx-3.2/wx/aboutdlg.h
/usr/include/wx-3.2/wx/accel.h
/usr/include/wx-3.2/wx/access.h
/usr/include/wx-3.2/wx/activityindicator.h
/usr/include/wx-3.2/wx/addremovectrl.h
/usr/include/wx-3.2/wx/affinematrix2d.h
/usr/include/wx-3.2/wx/affinematrix2dbase.h
/usr/include/wx-3.2/wx/afterstd.h
/usr/include/wx-3.2/wx/anidecod.h
/usr/include/wx-3.2/wx/animate.h
/usr/include/wx-3.2/wx/animdecod.h
/usr/include/wx-3.2/wx/any.h
/usr/include/wx-3.2/wx/anybutton.h
/usr/include/wx-3.2/wx/anystr.h
/usr/include/wx-3.2/wx/app.h
/usr/include/wx-3.2/wx/appprogress.h
/usr/include/wx-3.2/wx/apptrait.h
/usr/include/wx-3.2/wx/archive.h
/usr/include/wx-3.2/wx/arrimpl.cpp
/usr/include/wx-3.2/wx/arrstr.h
/usr/include/wx-3.2/wx/artprov.h
/usr/include/wx-3.2/wx/atomic.h
/usr/include/wx-3.2/wx/aui/aui.h
/usr/include/wx-3.2/wx/aui/auibar.h
/usr/include/wx-3.2/wx/aui/auibook.h
/usr/include/wx-3.2/wx/aui/dockart.h
/usr/include/wx-3.2/wx/aui/floatpane.h
/usr/include/wx-3.2/wx/aui/framemanager.h
/usr/include/wx-3.2/wx/aui/tabart.h
/usr/include/wx-3.2/wx/aui/tabmdi.h
/usr/include/wx-3.2/wx/bannerwindow.h
/usr/include/wx-3.2/wx/base64.h
/usr/include/wx-3.2/wx/beforestd.h
/usr/include/wx-3.2/wx/bitmap.h
/usr/include/wx-3.2/wx/bmpbndl.h
/usr/include/wx-3.2/wx/bmpbuttn.h
/usr/include/wx-3.2/wx/bmpcbox.h
/usr/include/wx-3.2/wx/bookctrl.h
/usr/include/wx-3.2/wx/brush.h
/usr/include/wx-3.2/wx/buffer.h
/usr/include/wx-3.2/wx/build.h
/usr/include/wx-3.2/wx/busyinfo.h
/usr/include/wx-3.2/wx/button.h
/usr/include/wx-3.2/wx/calctrl.h
/usr/include/wx-3.2/wx/caret.h
/usr/include/wx-3.2/wx/chartype.h
/usr/include/wx-3.2/wx/checkbox.h
/usr/include/wx-3.2/wx/checkeddelete.h
/usr/include/wx-3.2/wx/checklst.h
/usr/include/wx-3.2/wx/chkconf.h
/usr/include/wx-3.2/wx/choicdlg.h
/usr/include/wx-3.2/wx/choice.h
/usr/include/wx-3.2/wx/choicebk.h
/usr/include/wx-3.2/wx/clipbrd.h
/usr/include/wx-3.2/wx/clntdata.h
/usr/include/wx-3.2/wx/clrpicker.h
/usr/include/wx-3.2/wx/cmdargs.h
/usr/include/wx-3.2/wx/cmdline.h
/usr/include/wx-3.2/wx/cmdproc.h
/usr/include/wx-3.2/wx/cmndata.h
/usr/include/wx-3.2/wx/collheaderctrl.h
/usr/include/wx-3.2/wx/collpane.h
/usr/include/wx-3.2/wx/colordlg.h
/usr/include/wx-3.2/wx/colour.h
/usr/include/wx-3.2/wx/colourdata.h
/usr/include/wx-3.2/wx/combo.h
/usr/include/wx-3.2/wx/combobox.h
/usr/include/wx-3.2/wx/commandlinkbutton.h
/usr/include/wx-3.2/wx/compiler.h
/usr/include/wx-3.2/wx/compositewin.h
/usr/include/wx-3.2/wx/confbase.h
/usr/include/wx-3.2/wx/config.h
/usr/include/wx-3.2/wx/containr.h
/usr/include/wx-3.2/wx/control.h
/usr/include/wx-3.2/wx/convauto.h
/usr/include/wx-3.2/wx/cpp.h
/usr/include/wx-3.2/wx/creddlg.h
/usr/include/wx-3.2/wx/crt.h
/usr/include/wx-3.2/wx/cshelp.h
/usr/include/wx-3.2/wx/ctrlsub.h
/usr/include/wx-3.2/wx/cursor.h
/usr/include/wx-3.2/wx/custombgwin.h
/usr/include/wx-3.2/wx/dataobj.h
/usr/include/wx-3.2/wx/dataview.h
/usr/include/wx-3.2/wx/datectrl.h
/usr/include/wx-3.2/wx/dateevt.h
/usr/include/wx-3.2/wx/datetime.h
/usr/include/wx-3.2/wx/datetimectrl.h
/usr/include/wx-3.2/wx/datstrm.h
/usr/include/wx-3.2/wx/dc.h
/usr/include/wx-3.2/wx/dcbuffer.h
/usr/include/wx-3.2/wx/dcclient.h
/usr/include/wx-3.2/wx/dcgraph.h
/usr/include/wx-3.2/wx/dcmemory.h
/usr/include/wx-3.2/wx/dcmirror.h
/usr/include/wx-3.2/wx/dcprint.h
/usr/include/wx-3.2/wx/dcps.h
/usr/include/wx-3.2/wx/dcscreen.h
/usr/include/wx-3.2/wx/dcsvg.h
/usr/include/wx-3.2/wx/dde.h
/usr/include/wx-3.2/wx/debug.h
/usr/include/wx-3.2/wx/debugrpt.h
/usr/include/wx-3.2/wx/defs.h
/usr/include/wx-3.2/wx/dialog.h
/usr/include/wx-3.2/wx/dialup.h
/usr/include/wx-3.2/wx/dir.h
/usr/include/wx-3.2/wx/dirctrl.h
/usr/include/wx-3.2/wx/dirdlg.h
/usr/include/wx-3.2/wx/display.h
/usr/include/wx-3.2/wx/dlimpexp.h
/usr/include/wx-3.2/wx/dlist.h
/usr/include/wx-3.2/wx/dnd.h
/usr/include/wx-3.2/wx/docmdi.h
/usr/include/wx-3.2/wx/docview.h
/usr/include/wx-3.2/wx/dragimag.h
/usr/include/wx-3.2/wx/dvrenderers.h
/usr/include/wx-3.2/wx/dynarray.h
/usr/include/wx-3.2/wx/dynlib.h
/usr/include/wx-3.2/wx/dynload.h
/usr/include/wx-3.2/wx/editlbox.h
/usr/include/wx-3.2/wx/effects.h
/usr/include/wx-3.2/wx/encconv.h
/usr/include/wx-3.2/wx/encinfo.h
/usr/include/wx-3.2/wx/event.h
/usr/include/wx-3.2/wx/eventfilter.h
/usr/include/wx-3.2/wx/evtloop.h
/usr/include/wx-3.2/wx/evtloopsrc.h
/usr/include/wx-3.2/wx/except.h
/usr/include/wx-3.2/wx/fdrepdlg.h
/usr/include/wx-3.2/wx/features.h
/usr/include/wx-3.2/wx/ffile.h
/usr/include/wx-3.2/wx/file.h
/usr/include/wx-3.2/wx/fileconf.h
/usr/include/wx-3.2/wx/filectrl.h
/usr/include/wx-3.2/wx/filedlg.h
/usr/include/wx-3.2/wx/filedlgcustomize.h
/usr/include/wx-3.2/wx/filefn.h
/usr/include/wx-3.2/wx/filehistory.h
/usr/include/wx-3.2/wx/filename.h
/usr/include/wx-3.2/wx/filepicker.h
/usr/include/wx-3.2/wx/filesys.h
/usr/include/wx-3.2/wx/flags.h
/usr/include/wx-3.2/wx/fmappriv.h
/usr/include/wx-3.2/wx/font.h
/usr/include/wx-3.2/wx/fontdata.h
/usr/include/wx-3.2/wx/fontdlg.h
/usr/include/wx-3.2/wx/fontenc.h
/usr/include/wx-3.2/wx/fontenum.h
/usr/include/wx-3.2/wx/fontmap.h
/usr/include/wx-3.2/wx/fontpicker.h
/usr/include/wx-3.2/wx/fontutil.h
/usr/include/wx-3.2/wx/frame.h
/usr/include/wx-3.2/wx/fs_arc.h
/usr/include/wx-3.2/wx/fs_filter.h
/usr/include/wx-3.2/wx/fs_inet.h
/usr/include/wx-3.2/wx/fs_mem.h
/usr/include/wx-3.2/wx/fs_zip.h
/usr/include/wx-3.2/wx/fswatcher.h
/usr/include/wx-3.2/wx/gauge.h
/usr/include/wx-3.2/wx/gbsizer.h
/usr/include/wx-3.2/wx/gdicmn.h
/usr/include/wx-3.2/wx/gdiobj.h
/usr/include/wx-3.2/wx/generic/aboutdlgg.h
/usr/include/wx-3.2/wx/generic/accel.h
/usr/include/wx-3.2/wx/generic/activityindicator.h
/usr/include/wx-3.2/wx/generic/animate.h
/usr/include/wx-3.2/wx/generic/bmpcbox.h
/usr/include/wx-3.2/wx/generic/busyinfo.h
/usr/include/wx-3.2/wx/generic/buttonbar.h
/usr/include/wx-3.2/wx/generic/calctrlg.h
/usr/include/wx-3.2/wx/generic/caret.h
/usr/include/wx-3.2/wx/generic/choicdgg.h
/usr/include/wx-3.2/wx/generic/collheaderctrl.h
/usr/include/wx-3.2/wx/generic/combo.h
/usr/include/wx-3.2/wx/generic/creddlgg.h
/usr/include/wx-3.2/wx/generic/custombgwin.h
/usr/include/wx-3.2/wx/generic/dataview.h
/usr/include/wx-3.2/wx/generic/datectrl.h
/usr/include/wx-3.2/wx/generic/dcpsg.h
/usr/include/wx-3.2/wx/generic/dirctrlg.h
/usr/include/wx-3.2/wx/generic/dragimgg.h
/usr/include/wx-3.2/wx/generic/dvrenderer.h
/usr/include/wx-3.2/wx/generic/dvrenderers.h
/usr/include/wx-3.2/wx/generic/fdrepdlg.h
/usr/include/wx-3.2/wx/generic/filectrlg.h
/usr/include/wx-3.2/wx/generic/filepickerg.h
/usr/include/wx-3.2/wx/generic/fswatcher.h
/usr/include/wx-3.2/wx/generic/grid.h
/usr/include/wx-3.2/wx/generic/gridctrl.h
/usr/include/wx-3.2/wx/generic/grideditors.h
/usr/include/wx-3.2/wx/generic/gridsel.h
/usr/include/wx-3.2/wx/generic/headerctrlg.h
/usr/include/wx-3.2/wx/generic/helpext.h
/usr/include/wx-3.2/wx/generic/hyperlink.h
/usr/include/wx-3.2/wx/generic/icon.h
/usr/include/wx-3.2/wx/generic/imaglist.h
/usr/include/wx-3.2/wx/generic/infobar.h
/usr/include/wx-3.2/wx/generic/laywin.h
/usr/include/wx-3.2/wx/generic/listctrl.h
/usr/include/wx-3.2/wx/generic/logg.h
/usr/include/wx-3.2/wx/generic/msgdlgg.h
/usr/include/wx-3.2/wx/generic/notebook.h
/usr/include/wx-3.2/wx/generic/notifmsg.h
/usr/include/wx-3.2/wx/generic/numdlgg.h
/usr/include/wx-3.2/wx/generic/paletteg.h
/usr/include/wx-3.2/wx/generic/panelg.h
/usr/include/wx-3.2/wx/generic/printps.h
/usr/include/wx-3.2/wx/generic/prntdlgg.h
/usr/include/wx-3.2/wx/generic/progdlgg.h
/usr/include/wx-3.2/wx/generic/propdlg.h
/usr/include/wx-3.2/wx/generic/richmsgdlgg.h
/usr/include/wx-3.2/wx/generic/sashwin.h
/usr/include/wx-3.2/wx/generic/scrolwin.h
/usr/include/wx-3.2/wx/generic/spinctlg.h
/usr/include/wx-3.2/wx/generic/splash.h
/usr/include/wx-3.2/wx/generic/splitter.h
/usr/include/wx-3.2/wx/generic/srchctlg.h
/usr/include/wx-3.2/wx/generic/statbmpg.h
/usr/include/wx-3.2/wx/generic/stattextg.h
/usr/include/wx-3.2/wx/generic/statusbr.h
/usr/include/wx-3.2/wx/generic/textdlgg.h
/usr/include/wx-3.2/wx/generic/timectrl.h
/usr/include/wx-3.2/wx/generic/treectlg.h
/usr/include/wx-3.2/wx/generic/wizard.h
/usr/include/wx-3.2/wx/geometry.h
/usr/include/wx-3.2/wx/gifdecod.h
/usr/include/wx-3.2/wx/glcanvas.h
/usr/include/wx-3.2/wx/graphics.h
/usr/include/wx-3.2/wx/grid.h
/usr/include/wx-3.2/wx/gtk/accel.h
/usr/include/wx-3.2/wx/gtk/activityindicator.h
/usr/include/wx-3.2/wx/gtk/animate.h
/usr/include/wx-3.2/wx/gtk/anybutton.h
/usr/include/wx-3.2/wx/gtk/app.h
/usr/include/wx-3.2/wx/gtk/assertdlg_gtk.h
/usr/include/wx-3.2/wx/gtk/bitmap.h
/usr/include/wx-3.2/wx/gtk/bmpbuttn.h
/usr/include/wx-3.2/wx/gtk/bmpcbox.h
/usr/include/wx-3.2/wx/gtk/brush.h
/usr/include/wx-3.2/wx/gtk/button.h
/usr/include/wx-3.2/wx/gtk/calctrl.h
/usr/include/wx-3.2/wx/gtk/checkbox.h
/usr/include/wx-3.2/wx/gtk/checklst.h
/usr/include/wx-3.2/wx/gtk/chkconf.h
/usr/include/wx-3.2/wx/gtk/choice.h
/usr/include/wx-3.2/wx/gtk/clipbrd.h
/usr/include/wx-3.2/wx/gtk/clrpicker.h
/usr/include/wx-3.2/wx/gtk/collpane.h
/usr/include/wx-3.2/wx/gtk/colordlg.h
/usr/include/wx-3.2/wx/gtk/colour.h
/usr/include/wx-3.2/wx/gtk/combobox.h
/usr/include/wx-3.2/wx/gtk/control.h
/usr/include/wx-3.2/wx/gtk/cursor.h
/usr/include/wx-3.2/wx/gtk/dataform.h
/usr/include/wx-3.2/wx/gtk/dataobj.h
/usr/include/wx-3.2/wx/gtk/dataobj2.h
/usr/include/wx-3.2/wx/gtk/dataview.h
/usr/include/wx-3.2/wx/gtk/dialog.h
/usr/include/wx-3.2/wx/gtk/dirdlg.h
/usr/include/wx-3.2/wx/gtk/dnd.h
/usr/include/wx-3.2/wx/gtk/dvrenderer.h
/usr/include/wx-3.2/wx/gtk/dvrenderers.h
/usr/include/wx-3.2/wx/gtk/evtloop.h
/usr/include/wx-3.2/wx/gtk/evtloopsrc.h
/usr/include/wx-3.2/wx/gtk/filectrl.h
/usr/include/wx-3.2/wx/gtk/filedlg.h
/usr/include/wx-3.2/wx/gtk/filehistory.h
/usr/include/wx-3.2/wx/gtk/filepicker.h
/usr/include/wx-3.2/wx/gtk/font.h
/usr/include/wx-3.2/wx/gtk/fontdlg.h
/usr/include/wx-3.2/wx/gtk/fontpicker.h
/usr/include/wx-3.2/wx/gtk/frame.h
/usr/include/wx-3.2/wx/gtk/gauge.h
/usr/include/wx-3.2/wx/gtk/glcanvas.h
/usr/include/wx-3.2/wx/gtk/gnome/gvfs.h
/usr/include/wx-3.2/wx/gtk/hyperlink.h
/usr/include/wx-3.2/wx/gtk/infobar.h
/usr/include/wx-3.2/wx/gtk/listbox.h
/usr/include/wx-3.2/wx/gtk/mdi.h
/usr/include/wx-3.2/wx/gtk/menu.h
/usr/include/wx-3.2/wx/gtk/menuitem.h
/usr/include/wx-3.2/wx/gtk/mimetype.h
/usr/include/wx-3.2/wx/gtk/minifram.h
/usr/include/wx-3.2/wx/gtk/msgdlg.h
/usr/include/wx-3.2/wx/gtk/nonownedwnd.h
/usr/include/wx-3.2/wx/gtk/notebook.h
/usr/include/wx-3.2/wx/gtk/pen.h
/usr/include/wx-3.2/wx/gtk/popupwin.h
/usr/include/wx-3.2/wx/gtk/print.h
/usr/include/wx-3.2/wx/gtk/radiobox.h
/usr/include/wx-3.2/wx/gtk/radiobut.h
/usr/include/wx-3.2/wx/gtk/region.h
/usr/include/wx-3.2/wx/gtk/scrolbar.h
/usr/include/wx-3.2/wx/gtk/scrolwin.h
/usr/include/wx-3.2/wx/gtk/slider.h
/usr/include/wx-3.2/wx/gtk/spinbutt.h
/usr/include/wx-3.2/wx/gtk/spinctrl.h
/usr/include/wx-3.2/wx/gtk/srchctrl.h
/usr/include/wx-3.2/wx/gtk/statbmp.h
/usr/include/wx-3.2/wx/gtk/statbox.h
/usr/include/wx-3.2/wx/gtk/statline.h
/usr/include/wx-3.2/wx/gtk/stattext.h
/usr/include/wx-3.2/wx/gtk/taskbar.h
/usr/include/wx-3.2/wx/gtk/textctrl.h
/usr/include/wx-3.2/wx/gtk/textentry.h
/usr/include/wx-3.2/wx/gtk/tglbtn.h
/usr/include/wx-3.2/wx/gtk/toolbar.h
/usr/include/wx-3.2/wx/gtk/tooltip.h
/usr/include/wx-3.2/wx/gtk/toplevel.h
/usr/include/wx-3.2/wx/gtk/webview_webkit.h
/usr/include/wx-3.2/wx/gtk/webviewhistoryitem_webkit.h
/usr/include/wx-3.2/wx/gtk/window.h
/usr/include/wx-3.2/wx/hash.h
/usr/include/wx-3.2/wx/hashmap.h
/usr/include/wx-3.2/wx/hashset.h
/usr/include/wx-3.2/wx/headercol.h
/usr/include/wx-3.2/wx/headerctrl.h
/usr/include/wx-3.2/wx/help.h
/usr/include/wx-3.2/wx/helpbase.h
/usr/include/wx-3.2/wx/helphtml.h
/usr/include/wx-3.2/wx/helpwin.h
/usr/include/wx-3.2/wx/html/forcelnk.h
/usr/include/wx-3.2/wx/html/helpctrl.h
/usr/include/wx-3.2/wx/html/helpdata.h
/usr/include/wx-3.2/wx/html/helpdlg.h
/usr/include/wx-3.2/wx/html/helpfrm.h
/usr/include/wx-3.2/wx/html/helpwnd.h
/usr/include/wx-3.2/wx/html/htmlcell.h
/usr/include/wx-3.2/wx/html/htmldefs.h
/usr/include/wx-3.2/wx/html/htmlfilt.h
/usr/include/wx-3.2/wx/html/htmlpars.h
/usr/include/wx-3.2/wx/html/htmlproc.h
/usr/include/wx-3.2/wx/html/htmltag.h
/usr/include/wx-3.2/wx/html/htmlwin.h
/usr/include/wx-3.2/wx/html/htmprint.h
/usr/include/wx-3.2/wx/html/m_templ.h
/usr/include/wx-3.2/wx/html/styleparams.h
/usr/include/wx-3.2/wx/html/winpars.h
/usr/include/wx-3.2/wx/htmllbox.h
/usr/include/wx-3.2/wx/hyperlink.h
/usr/include/wx-3.2/wx/icon.h
/usr/include/wx-3.2/wx/iconbndl.h
/usr/include/wx-3.2/wx/iconloc.h
/usr/include/wx-3.2/wx/imagbmp.h
/usr/include/wx-3.2/wx/image.h
/usr/include/wx-3.2/wx/imaggif.h
/usr/include/wx-3.2/wx/imagiff.h
/usr/include/wx-3.2/wx/imagjpeg.h
/usr/include/wx-3.2/wx/imaglist.h
/usr/include/wx-3.2/wx/imagpcx.h
/usr/include/wx-3.2/wx/imagpng.h
/usr/include/wx-3.2/wx/imagpnm.h
/usr/include/wx-3.2/wx/imagtga.h
/usr/include/wx-3.2/wx/imagtiff.h
/usr/include/wx-3.2/wx/imagxpm.h
/usr/include/wx-3.2/wx/infobar.h
/usr/include/wx-3.2/wx/init.h
/usr/include/wx-3.2/wx/intl.h
/usr/include/wx-3.2/wx/iosfwrap.h
/usr/include/wx-3.2/wx/ioswrap.h
/usr/include/wx-3.2/wx/ipc.h
/usr/include/wx-3.2/wx/ipcbase.h
/usr/include/wx-3.2/wx/itemattr.h
/usr/include/wx-3.2/wx/itemid.h
/usr/include/wx-3.2/wx/joystick.h
/usr/include/wx-3.2/wx/kbdstate.h
/usr/include/wx-3.2/wx/language.h
/usr/include/wx-3.2/wx/layout.h
/usr/include/wx-3.2/wx/laywin.h
/usr/include/wx-3.2/wx/link.h
/usr/include/wx-3.2/wx/list.h
/usr/include/wx-3.2/wx/listbase.h
/usr/include/wx-3.2/wx/listbook.h
/usr/include/wx-3.2/wx/listbox.h
/usr/include/wx-3.2/wx/listctrl.h
/usr/include/wx-3.2/wx/listimpl.cpp
/usr/include/wx-3.2/wx/localedefs.h
/usr/include/wx-3.2/wx/log.h
/usr/include/wx-3.2/wx/longlong.h
/usr/include/wx-3.2/wx/lzmastream.h
/usr/include/wx-3.2/wx/math.h
/usr/include/wx-3.2/wx/matrix.h
/usr/include/wx-3.2/wx/mdi.h
/usr/include/wx-3.2/wx/mediactrl.h
/usr/include/wx-3.2/wx/memconf.h
/usr/include/wx-3.2/wx/memory.h
/usr/include/wx-3.2/wx/memtext.h
/usr/include/wx-3.2/wx/menu.h
/usr/include/wx-3.2/wx/menuitem.h
/usr/include/wx-3.2/wx/meta/convertible.h
/usr/include/wx-3.2/wx/meta/if.h
/usr/include/wx-3.2/wx/meta/implicitconversion.h
/usr/include/wx-3.2/wx/meta/int2type.h
/usr/include/wx-3.2/wx/meta/movable.h
/usr/include/wx-3.2/wx/meta/pod.h
/usr/include/wx-3.2/wx/meta/removeref.h
/usr/include/wx-3.2/wx/metafile.h
/usr/include/wx-3.2/wx/mimetype.h
/usr/include/wx-3.2/wx/minifram.h
/usr/include/wx-3.2/wx/modalhook.h
/usr/include/wx-3.2/wx/module.h
/usr/include/wx-3.2/wx/mousemanager.h
/usr/include/wx-3.2/wx/mousestate.h
/usr/include/wx-3.2/wx/msgdlg.h
/usr/include/wx-3.2/wx/msgout.h
/usr/include/wx-3.2/wx/msgqueue.h
/usr/include/wx-3.2/wx/mstream.h
/usr/include/wx-3.2/wx/nativewin.h
/usr/include/wx-3.2/wx/nonownedwnd.h
/usr/include/wx-3.2/wx/notebook.h
/usr/include/wx-3.2/wx/notifmsg.h
/usr/include/wx-3.2/wx/numdlg.h
/usr/include/wx-3.2/wx/numformatter.h
/usr/include/wx-3.2/wx/object.h
/usr/include/wx-3.2/wx/odcombo.h
/usr/include/wx-3.2/wx/overlay.h
/usr/include/wx-3.2/wx/ownerdrw.h
/usr/include/wx-3.2/wx/palette.h
/usr/include/wx-3.2/wx/panel.h
/usr/include/wx-3.2/wx/paper.h
/usr/include/wx-3.2/wx/pen.h
/usr/include/wx-3.2/wx/peninfobase.h
/usr/include/wx-3.2/wx/persist.h
/usr/include/wx-3.2/wx/persist/bookctrl.h
/usr/include/wx-3.2/wx/persist/dataview.h
/usr/include/wx-3.2/wx/persist/splitter.h
/usr/include/wx-3.2/wx/persist/toplevel.h
/usr/include/wx-3.2/wx/persist/treebook.h
/usr/include/wx-3.2/wx/persist/window.h
/usr/include/wx-3.2/wx/pickerbase.h
/usr/include/wx-3.2/wx/platform.h
/usr/include/wx-3.2/wx/platinfo.h
/usr/include/wx-3.2/wx/popupwin.h
/usr/include/wx-3.2/wx/position.h
/usr/include/wx-3.2/wx/power.h
/usr/include/wx-3.2/wx/preferences.h
/usr/include/wx-3.2/wx/print.h
/usr/include/wx-3.2/wx/printdlg.h
/usr/include/wx-3.2/wx/prntbase.h
/usr/include/wx-3.2/wx/process.h
/usr/include/wx-3.2/wx/progdlg.h
/usr/include/wx-3.2/wx/propdlg.h
/usr/include/wx-3.2/wx/propgrid/advprops.h
/usr/include/wx-3.2/wx/propgrid/editors.h
/usr/include/wx-3.2/wx/propgrid/manager.h
/usr/include/wx-3.2/wx/propgrid/property.h
/usr/include/wx-3.2/wx/propgrid/propgrid.h
/usr/include/wx-3.2/wx/propgrid/propgriddefs.h
/usr/include/wx-3.2/wx/propgrid/propgridiface.h
/usr/include/wx-3.2/wx/propgrid/propgridpagestate.h
/usr/include/wx-3.2/wx/propgrid/props.h
/usr/include/wx-3.2/wx/protocol/file.h
/usr/include/wx-3.2/wx/protocol/ftp.h
/usr/include/wx-3.2/wx/protocol/http.h
/usr/include/wx-3.2/wx/protocol/log.h
/usr/include/wx-3.2/wx/protocol/protocol.h
/usr/include/wx-3.2/wx/ptr_scpd.h
/usr/include/wx-3.2/wx/ptr_shrd.h
/usr/include/wx-3.2/wx/quantize.h
/usr/include/wx-3.2/wx/radiobox.h
/usr/include/wx-3.2/wx/radiobut.h
/usr/include/wx-3.2/wx/range.h
/usr/include/wx-3.2/wx/rawbmp.h
/usr/include/wx-3.2/wx/rearrangectrl.h
/usr/include/wx-3.2/wx/recguard.h
/usr/include/wx-3.2/wx/regex.h
/usr/include/wx-3.2/wx/region.h
/usr/include/wx-3.2/wx/renderer.h
/usr/include/wx-3.2/wx/ribbon/art.h
/usr/include/wx-3.2/wx/ribbon/art_internal.h
/usr/include/wx-3.2/wx/ribbon/bar.h
/usr/include/wx-3.2/wx/ribbon/buttonbar.h
/usr/include/wx-3.2/wx/ribbon/control.h
/usr/include/wx-3.2/wx/ribbon/gallery.h
/usr/include/wx-3.2/wx/ribbon/page.h
/usr/include/wx-3.2/wx/ribbon/panel.h
/usr/include/wx-3.2/wx/ribbon/toolbar.h
/usr/include/wx-3.2/wx/richmsgdlg.h
/usr/include/wx-3.2/wx/richtext/richtextbackgroundpage.h
/usr/include/wx-3.2/wx/richtext/richtextborderspage.h
/usr/include/wx-3.2/wx/richtext/richtextbuffer.h
/usr/include/wx-3.2/wx/richtext/richtextbulletspage.h
/usr/include/wx-3.2/wx/richtext/richtextctrl.h
/usr/include/wx-3.2/wx/richtext/richtextdialogpage.h
/usr/include/wx-3.2/wx/richtext/richtextfontpage.h
/usr/include/wx-3.2/wx/richtext/richtextformatdlg.h
/usr/include/wx-3.2/wx/richtext/richtexthtml.h
/usr/include/wx-3.2/wx/richtext/richtextimagedlg.h
/usr/include/wx-3.2/wx/richtext/richtextindentspage.h
/usr/include/wx-3.2/wx/richtext/richtextliststylepage.h
/usr/include/wx-3.2/wx/richtext/richtextmarginspage.h
/usr/include/wx-3.2/wx/richtext/richtextprint.h
/usr/include/wx-3.2/wx/richtext/richtextsizepage.h
/usr/include/wx-3.2/wx/richtext/richtextstyledlg.h
/usr/include/wx-3.2/wx/richtext/richtextstylepage.h
/usr/include/wx-3.2/wx/richtext/richtextstyles.h
/usr/include/wx-3.2/wx/richtext/richtextsymboldlg.h
/usr/include/wx-3.2/wx/richtext/richtexttabspage.h
/usr/include/wx-3.2/wx/richtext/richtextuicustomization.h
/usr/include/wx-3.2/wx/richtext/richtextxml.h
/usr/include/wx-3.2/wx/richtooltip.h
/usr/include/wx-3.2/wx/rtti.h
/usr/include/wx-3.2/wx/sashwin.h
/usr/include/wx-3.2/wx/sckaddr.h
/usr/include/wx-3.2/wx/sckipc.h
/usr/include/wx-3.2/wx/sckstrm.h
/usr/include/wx-3.2/wx/scopedarray.h
/usr/include/wx-3.2/wx/scopedptr.h
/usr/include/wx-3.2/wx/scopeguard.h
/usr/include/wx-3.2/wx/scrolbar.h
/usr/include/wx-3.2/wx/scrolwin.h
/usr/include/wx-3.2/wx/secretstore.h
/usr/include/wx-3.2/wx/selstore.h
/usr/include/wx-3.2/wx/settings.h
/usr/include/wx-3.2/wx/sharedptr.h
/usr/include/wx-3.2/wx/simplebook.h
/usr/include/wx-3.2/wx/sizer.h
/usr/include/wx-3.2/wx/slider.h
/usr/include/wx-3.2/wx/snglinst.h
/usr/include/wx-3.2/wx/socket.h
/usr/include/wx-3.2/wx/sound.h
/usr/include/wx-3.2/wx/spinbutt.h
/usr/include/wx-3.2/wx/spinctrl.h
/usr/include/wx-3.2/wx/splash.h
/usr/include/wx-3.2/wx/splitter.h
/usr/include/wx-3.2/wx/srchctrl.h
/usr/include/wx-3.2/wx/sstream.h
/usr/include/wx-3.2/wx/stack.h
/usr/include/wx-3.2/wx/stackwalk.h
/usr/include/wx-3.2/wx/statbmp.h
/usr/include/wx-3.2/wx/statbox.h
/usr/include/wx-3.2/wx/statline.h
/usr/include/wx-3.2/wx/stattext.h
/usr/include/wx-3.2/wx/statusbr.h
/usr/include/wx-3.2/wx/stc/stc.h
/usr/include/wx-3.2/wx/stdpaths.h
/usr/include/wx-3.2/wx/stdstream.h
/usr/include/wx-3.2/wx/stockitem.h
/usr/include/wx-3.2/wx/stopwatch.h
/usr/include/wx-3.2/wx/strconv.h
/usr/include/wx-3.2/wx/stream.h
/usr/include/wx-3.2/wx/string.h
/usr/include/wx-3.2/wx/stringimpl.h
/usr/include/wx-3.2/wx/stringops.h
/usr/include/wx-3.2/wx/strvararg.h
/usr/include/wx-3.2/wx/sysopt.h
/usr/include/wx-3.2/wx/systhemectrl.h
/usr/include/wx-3.2/wx/tarstrm.h
/usr/include/wx-3.2/wx/taskbar.h
/usr/include/wx-3.2/wx/taskbarbutton.h
/usr/include/wx-3.2/wx/tbarbase.h
/usr/include/wx-3.2/wx/testing.h
/usr/include/wx-3.2/wx/textbuf.h
/usr/include/wx-3.2/wx/textcompleter.h
/usr/include/wx-3.2/wx/textctrl.h
/usr/include/wx-3.2/wx/textdlg.h
/usr/include/wx-3.2/wx/textentry.h
/usr/include/wx-3.2/wx/textfile.h
/usr/include/wx-3.2/wx/textwrapper.h
/usr/include/wx-3.2/wx/tglbtn.h
/usr/include/wx-3.2/wx/thread.h
/usr/include/wx-3.2/wx/thrimpl.cpp
/usr/include/wx-3.2/wx/time.h
/usr/include/wx-3.2/wx/timectrl.h
/usr/include/wx-3.2/wx/timer.h
/usr/include/wx-3.2/wx/tipdlg.h
/usr/include/wx-3.2/wx/tipwin.h
/usr/include/wx-3.2/wx/tls.h
/usr/include/wx-3.2/wx/tokenzr.h
/usr/include/wx-3.2/wx/toolbar.h
/usr/include/wx-3.2/wx/toolbook.h
/usr/include/wx-3.2/wx/tooltip.h
/usr/include/wx-3.2/wx/toplevel.h
/usr/include/wx-3.2/wx/tracker.h
/usr/include/wx-3.2/wx/translation.h
/usr/include/wx-3.2/wx/treebase.h
/usr/include/wx-3.2/wx/treebook.h
/usr/include/wx-3.2/wx/treectrl.h
/usr/include/wx-3.2/wx/treelist.h
/usr/include/wx-3.2/wx/txtstrm.h
/usr/include/wx-3.2/wx/typeinfo.h
/usr/include/wx-3.2/wx/types.h
/usr/include/wx-3.2/wx/uiaction.h
/usr/include/wx-3.2/wx/uilocale.h
/usr/include/wx-3.2/wx/unichar.h
/usr/include/wx-3.2/wx/unix/app.h
/usr/include/wx-3.2/wx/unix/apptbase.h
/usr/include/wx-3.2/wx/unix/apptrait.h
/usr/include/wx-3.2/wx/unix/chkconf.h
/usr/include/wx-3.2/wx/unix/evtloop.h
/usr/include/wx-3.2/wx/unix/evtloopsrc.h
/usr/include/wx-3.2/wx/unix/fontutil.h
/usr/include/wx-3.2/wx/unix/fswatcher_inotify.h
/usr/include/wx-3.2/wx/unix/fswatcher_kqueue.h
/usr/include/wx-3.2/wx/unix/glegl.h
/usr/include/wx-3.2/wx/unix/glx11.h
/usr/include/wx-3.2/wx/unix/joystick.h
/usr/include/wx-3.2/wx/unix/mimetype.h
/usr/include/wx-3.2/wx/unix/pipe.h
/usr/include/wx-3.2/wx/unix/sound.h
/usr/include/wx-3.2/wx/unix/stackwalk.h
/usr/include/wx-3.2/wx/unix/stdpaths.h
/usr/include/wx-3.2/wx/unix/taskbarx11.h
/usr/include/wx-3.2/wx/unix/tls.h
/usr/include/wx-3.2/wx/unix/utilsx11.h
/usr/include/wx-3.2/wx/uri.h
/usr/include/wx-3.2/wx/url.h
/usr/include/wx-3.2/wx/ustring.h
/usr/include/wx-3.2/wx/utils.h
/usr/include/wx-3.2/wx/valgen.h
/usr/include/wx-3.2/wx/validate.h
/usr/include/wx-3.2/wx/valnum.h
/usr/include/wx-3.2/wx/valtext.h
/usr/include/wx-3.2/wx/variant.h
/usr/include/wx-3.2/wx/vector.h
/usr/include/wx-3.2/wx/version.h
/usr/include/wx-3.2/wx/versioninfo.h
/usr/include/wx-3.2/wx/vidmode.h
/usr/include/wx-3.2/wx/vlbox.h
/usr/include/wx-3.2/wx/vms_x_fix.h
/usr/include/wx-3.2/wx/volume.h
/usr/include/wx-3.2/wx/vscroll.h
/usr/include/wx-3.2/wx/weakref.h
/usr/include/wx-3.2/wx/webrequest.h
/usr/include/wx-3.2/wx/webview.h
/usr/include/wx-3.2/wx/webviewarchivehandler.h
/usr/include/wx-3.2/wx/webviewfshandler.h
/usr/include/wx-3.2/wx/wfstream.h
/usr/include/wx-3.2/wx/window.h
/usr/include/wx-3.2/wx/windowid.h
/usr/include/wx-3.2/wx/windowptr.h
/usr/include/wx-3.2/wx/withimages.h
/usr/include/wx-3.2/wx/wizard.h
/usr/include/wx-3.2/wx/wrapsizer.h
/usr/include/wx-3.2/wx/wupdlock.h
/usr/include/wx-3.2/wx/wx.h
/usr/include/wx-3.2/wx/wxchar.h
/usr/include/wx-3.2/wx/wxcrt.h
/usr/include/wx-3.2/wx/wxcrtbase.h
/usr/include/wx-3.2/wx/wxcrtvararg.h
/usr/include/wx-3.2/wx/wxhtml.h
/usr/include/wx-3.2/wx/wxprec.h
/usr/include/wx-3.2/wx/xlocale.h
/usr/include/wx-3.2/wx/xml/xml.h
/usr/include/wx-3.2/wx/xpmdecod.h
/usr/include/wx-3.2/wx/xpmhand.h
/usr/include/wx-3.2/wx/xrc/xh_activityindicator.h
/usr/include/wx-3.2/wx/xrc/xh_all.h
/usr/include/wx-3.2/wx/xrc/xh_animatctrl.h
/usr/include/wx-3.2/wx/xrc/xh_aui.h
/usr/include/wx-3.2/wx/xrc/xh_auitoolb.h
/usr/include/wx-3.2/wx/xrc/xh_bannerwindow.h
/usr/include/wx-3.2/wx/xrc/xh_bmp.h
/usr/include/wx-3.2/wx/xrc/xh_bmpbt.h
/usr/include/wx-3.2/wx/xrc/xh_bmpcbox.h
/usr/include/wx-3.2/wx/xrc/xh_bookctrlbase.h
/usr/include/wx-3.2/wx/xrc/xh_bttn.h
/usr/include/wx-3.2/wx/xrc/xh_cald.h
/usr/include/wx-3.2/wx/xrc/xh_chckb.h
/usr/include/wx-3.2/wx/xrc/xh_chckl.h
/usr/include/wx-3.2/wx/xrc/xh_choic.h
/usr/include/wx-3.2/wx/xrc/xh_choicbk.h
/usr/include/wx-3.2/wx/xrc/xh_clrpicker.h
/usr/include/wx-3.2/wx/xrc/xh_cmdlinkbn.h
/usr/include/wx-3.2/wx/xrc/xh_collpane.h
/usr/include/wx-3.2/wx/xrc/xh_combo.h
/usr/include/wx-3.2/wx/xrc/xh_comboctrl.h
/usr/include/wx-3.2/wx/xrc/xh_dataview.h
/usr/include/wx-3.2/wx/xrc/xh_datectrl.h
/usr/include/wx-3.2/wx/xrc/xh_dirpicker.h
/usr/include/wx-3.2/wx/xrc/xh_dlg.h
/usr/include/wx-3.2/wx/xrc/xh_editlbox.h
/usr/include/wx-3.2/wx/xrc/xh_filectrl.h
/usr/include/wx-3.2/wx/xrc/xh_filepicker.h
/usr/include/wx-3.2/wx/xrc/xh_fontpicker.h
/usr/include/wx-3.2/wx/xrc/xh_frame.h
/usr/include/wx-3.2/wx/xrc/xh_gauge.h
/usr/include/wx-3.2/wx/xrc/xh_gdctl.h
/usr/include/wx-3.2/wx/xrc/xh_grid.h
/usr/include/wx-3.2/wx/xrc/xh_html.h
/usr/include/wx-3.2/wx/xrc/xh_htmllbox.h
/usr/include/wx-3.2/wx/xrc/xh_hyperlink.h
/usr/include/wx-3.2/wx/xrc/xh_infobar.h
/usr/include/wx-3.2/wx/xrc/xh_listb.h
/usr/include/wx-3.2/wx/xrc/xh_listbk.h
/usr/include/wx-3.2/wx/xrc/xh_listc.h
/usr/include/wx-3.2/wx/xrc/xh_mdi.h
/usr/include/wx-3.2/wx/xrc/xh_menu.h
/usr/include/wx-3.2/wx/xrc/xh_notbk.h
/usr/include/wx-3.2/wx/xrc/xh_odcombo.h
/usr/include/wx-3.2/wx/xrc/xh_panel.h
/usr/include/wx-3.2/wx/xrc/xh_propdlg.h
/usr/include/wx-3.2/wx/xrc/xh_radbt.h
/usr/include/wx-3.2/wx/xrc/xh_radbx.h
/usr/include/wx-3.2/wx/xrc/xh_ribbon.h
/usr/include/wx-3.2/wx/xrc/xh_richtext.h
/usr/include/wx-3.2/wx/xrc/xh_scrol.h
/usr/include/wx-3.2/wx/xrc/xh_scwin.h
/usr/include/wx-3.2/wx/xrc/xh_simplebook.h
/usr/include/wx-3.2/wx/xrc/xh_sizer.h
/usr/include/wx-3.2/wx/xrc/xh_slidr.h
/usr/include/wx-3.2/wx/xrc/xh_spin.h
/usr/include/wx-3.2/wx/xrc/xh_split.h
/usr/include/wx-3.2/wx/xrc/xh_srchctrl.h
/usr/include/wx-3.2/wx/xrc/xh_statbar.h
/usr/include/wx-3.2/wx/xrc/xh_stbmp.h
/usr/include/wx-3.2/wx/xrc/xh_stbox.h
/usr/include/wx-3.2/wx/xrc/xh_stlin.h
/usr/include/wx-3.2/wx/xrc/xh_sttxt.h
/usr/include/wx-3.2/wx/xrc/xh_styledtextctrl.h
/usr/include/wx-3.2/wx/xrc/xh_text.h
/usr/include/wx-3.2/wx/xrc/xh_tglbtn.h
/usr/include/wx-3.2/wx/xrc/xh_timectrl.h
/usr/include/wx-3.2/wx/xrc/xh_toolb.h
/usr/include/wx-3.2/wx/xrc/xh_toolbk.h
/usr/include/wx-3.2/wx/xrc/xh_tree.h
/usr/include/wx-3.2/wx/xrc/xh_treebk.h
/usr/include/wx-3.2/wx/xrc/xh_unkwn.h
/usr/include/wx-3.2/wx/xrc/xh_wizrd.h
/usr/include/wx-3.2/wx/xrc/xmlres.h
/usr/include/wx-3.2/wx/xrc/xmlreshandler.h
/usr/include/wx-3.2/wx/xti.h
/usr/include/wx-3.2/wx/xti2.h
/usr/include/wx-3.2/wx/xtictor.h
/usr/include/wx-3.2/wx/xtihandler.h
/usr/include/wx-3.2/wx/xtiprop.h
/usr/include/wx-3.2/wx/xtistrm.h
/usr/include/wx-3.2/wx/xtitypes.h
/usr/include/wx-3.2/wx/xtixml.h
/usr/include/wx-3.2/wx/zipstrm.h
/usr/include/wx-3.2/wx/zstream.h
/usr/lib64/libwx_baseu-3.2.so
/usr/lib64/libwx_baseu_net-3.2.so
/usr/lib64/libwx_baseu_xml-3.2.so
/usr/lib64/libwx_gtk3u_adv-3.2.so
/usr/lib64/libwx_gtk3u_aui-3.2.so
/usr/lib64/libwx_gtk3u_core-3.2.so
/usr/lib64/libwx_gtk3u_gl-3.2.so
/usr/lib64/libwx_gtk3u_html-3.2.so
/usr/lib64/libwx_gtk3u_media-3.2.so
/usr/lib64/libwx_gtk3u_propgrid-3.2.so
/usr/lib64/libwx_gtk3u_qa-3.2.so
/usr/lib64/libwx_gtk3u_ribbon-3.2.so
/usr/lib64/libwx_gtk3u_richtext-3.2.so
/usr/lib64/libwx_gtk3u_stc-3.2.so
/usr/lib64/libwx_gtk3u_xrc-3.2.so
/usr/lib64/wx/include/gtk3-unicode-3.2/wx/setup.h
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libwx_baseu-3.2.so.0.2.1
/V3/usr/lib64/libwx_baseu_net-3.2.so.0.2.1
/V3/usr/lib64/libwx_baseu_xml-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_adv-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_aui-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_core-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_gl-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_html-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_media-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_propgrid-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_qa-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_ribbon-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_richtext-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_stc-3.2.so.0.2.1
/V3/usr/lib64/libwx_gtk3u_xrc-3.2.so.0.2.1
/usr/lib64/libwx_baseu-3.2.so.0
/usr/lib64/libwx_baseu-3.2.so.0.2.1
/usr/lib64/libwx_baseu_net-3.2.so.0
/usr/lib64/libwx_baseu_net-3.2.so.0.2.1
/usr/lib64/libwx_baseu_xml-3.2.so.0
/usr/lib64/libwx_baseu_xml-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_adv-3.2.so.0
/usr/lib64/libwx_gtk3u_adv-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_aui-3.2.so.0
/usr/lib64/libwx_gtk3u_aui-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_core-3.2.so.0
/usr/lib64/libwx_gtk3u_core-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_gl-3.2.so.0
/usr/lib64/libwx_gtk3u_gl-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_html-3.2.so.0
/usr/lib64/libwx_gtk3u_html-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_media-3.2.so.0
/usr/lib64/libwx_gtk3u_media-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_propgrid-3.2.so.0
/usr/lib64/libwx_gtk3u_propgrid-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_qa-3.2.so.0
/usr/lib64/libwx_gtk3u_qa-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_ribbon-3.2.so.0
/usr/lib64/libwx_gtk3u_ribbon-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_richtext-3.2.so.0
/usr/lib64/libwx_gtk3u_richtext-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_stc-3.2.so.0
/usr/lib64/libwx_gtk3u_stc-3.2.so.0.2.1
/usr/lib64/libwx_gtk3u_xrc-3.2.so.0
/usr/lib64/libwx_gtk3u_xrc-3.2.so.0.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wxWidgets/17e3b0eea99abffe6ac71e65627413236e0b117a
/usr/share/package-licenses/wxWidgets/3005b2c68faac406829c8ea56376ddcb1ed0eabb
/usr/share/package-licenses/wxWidgets/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/wxWidgets/3f65d8e23a75d7c0a9a7b7092c9249e4f8cd2db4
/usr/share/package-licenses/wxWidgets/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/wxWidgets/8623dd26727a708a49dbe6a52edb1d931d70816d
/usr/share/package-licenses/wxWidgets/9a5a0d7c8ffa82a9489acbb7f0d6947a2b1bc27f
/usr/share/package-licenses/wxWidgets/9da27f7b263edb706105ccd68880474013b11bca
/usr/share/package-licenses/wxWidgets/a2f64f2a85f5fd34bda8eb713c3aad008adbb589
/usr/share/package-licenses/wxWidgets/ec2350cf4fe9c4f97c3ee5c9046d0396672c365a
/usr/share/package-licenses/wxWidgets/ece76272e705e27f0c76531aac6dd0b10820bc10
/usr/share/package-licenses/wxWidgets/f4f94babc436555d2f5992e29aacc47433fbadb4
/usr/share/package-licenses/wxWidgets/fc3951ba26fe1914759f605696a1d23e3b41766f
/usr/share/package-licenses/wxWidgets/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f wxstd-3.2.lang
%defattr(-,root,root,-)

