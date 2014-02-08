# revision 26689
# category TLCore
# catalog-ctan /support/ps2eps
# catalog-date 2010-08-31 15:53:08 +0200
# catalog-license gpl
# catalog-version 1.68
Name:		texlive-pstools
Version:	1.68
Release:	5
Summary:	Produce Encapsulated PostScript from PostScript
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/ps2eps
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstools.x86_64-linux.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-pstools.bin
%rename ps2eps

%description
Produce Encapsulated PostScript Files (EPS/EPSF) from a one-
page PostScript document, or any PostScript document. A correct
Bounding Box is calculated for the EPS files and some
PostScript command sequences that can produce errorneous
results on printers are filtered. The input is cropped to
include just the image contained in the PostScript file. The
EPS files can then be included into TeX documents. Other
programs like ps2epsi (a script distributed with ghostscript)
don't always calculate the correct bounding box (because the
values are put on the PostScript stack which may get corrupted
by bad PostScript code) or they round it off, resulting in
clipping the image. Therefore ps2eps uses a resolution of 144
dpi to get the correct bounding box. ps2eps needs perl,
ghostscript and an ANSI-C compiler if your platform is not
Linux, Solaris, Digital Unix or Windows 2000/9x/NT (for which
binaries are included). Included in the distribution is the
bbox program, an application to produce Bounding Box values for
rawppm or rawpbm format files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/ps2eps
%{_bindir}/ps2frag
%{_bindir}/pslatex
%{_texmfdir}/scripts/ps2eps/ps2eps.pl
%doc %{_mandir}/man1/bbox.1*
%doc %{_texmfdir}/doc/man/man1/bbox.man1.pdf
%doc %{_mandir}/man1/ps2eps.1*
%doc %{_texmfdir}/doc/man/man1/ps2eps.man1.pdf
%doc %{_mandir}/man1/ps2frag.1*
%doc %{_texmfdir}/doc/man/man1/ps2frag.man1.pdf
%doc %{_mandir}/man1/pslatex.1*
%doc %{_texmfdir}/doc/man/man1/pslatex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
# 2 scripts and one binary
mkdir -p %{buildroot}%{_bindir}
cp -f bin/x86_64-linux/ps2frag bin/x86_64-linux/pslatex %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/ps2eps/ps2eps.pl ps2eps
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.68-4
+ Revision: 812809
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.68-3
+ Revision: 755389
- Rebuild to reduce used resources

* Sun Nov 13 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.68-2
+ Revision: 730330
- Use rename macro instead of mix of provides/conflicts/obsoletes

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.68-1
+ Revision: 719373
- texlive-pstools
- texlive-pstools
- texlive-pstools
- texlive-pstools

