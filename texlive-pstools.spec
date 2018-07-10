# revision 33736
# category TLCore
# catalog-ctan /support/ps2eps
# catalog-date 2012-07-20 20:39:39 +0200
# catalog-license gpl
# catalog-version 1.68
Name:		texlive-pstools
Version:	1.68
Release:	16
Summary:	Produce Encapsulated PostScript from PostScript
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/ps2eps
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstools.doc.tar.xz
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
dpi to get the correct bounding box. The bundle includes
binaries for Linux, Solaris, Digital Unix or Windows
2000/9x/NT; for other platforms, the user needs perl,
ghostscript and an ANSI-C compiler. Included in the
distribution is the bbox program, an application to produce
Bounding Box values for rawppm or rawpbm format files.

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
%{_texmfdistdir}/scripts/ps2eps/ps2eps.pl
%{_texmfdistdir}/scripts/texlive/ps2frag.sh
%{_texmfdistdir}/scripts/texlive/pslatex.sh
%doc %{_mandir}/man1/bbox.1*
%doc %{_texmfdistdir}/doc/man/man1/bbox.man1.pdf
%doc %{_mandir}/man1/ps2eps.1*
%doc %{_texmfdistdir}/doc/man/man1/ps2eps.man1.pdf
%doc %{_mandir}/man1/ps2frag.1*
%doc %{_texmfdistdir}/doc/man/man1/ps2frag.man1.pdf
%doc %{_mandir}/man1/pslatex.1*
%doc %{_texmfdistdir}/doc/man/man1/pslatex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/ps2eps/ps2eps.pl ps2eps
    ln -sf %{_texmfdistdir}/scripts/texlive/ps2frag.sh ps2frag
    ln -sf %{_texmfdistdir}/scripts/texlive/pslatex.sh pslatex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
