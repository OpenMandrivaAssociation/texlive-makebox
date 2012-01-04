# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/makebox
# catalog-date 2006-12-02 14:51:32 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-makebox
Version:	0.1
Release:	2
Summary:	Defines a \makebox* command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makebox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Define a \makebox* command that does the same as a \makebox
command, except that the width is given by a sample text
instead of an explicit length measure.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makebox/makebox.sty
%doc %{_texmfdistdir}/doc/latex/makebox/ChangeLog
%doc %{_texmfdistdir}/doc/latex/makebox/README
%doc %{_texmfdistdir}/doc/latex/makebox/getversion.tex
%doc %{_texmfdistdir}/doc/latex/makebox/makebox.pdf
%doc %{_texmfdistdir}/doc/latex/makebox/makebox.xml
%doc %{_texmfdistdir}/doc/latex/makebox/testmakebox.tex
#- source
%doc %{_texmfdistdir}/source/latex/makebox/Makefile
%doc %{_texmfdistdir}/source/latex/makebox/makebox.dtx
%doc %{_texmfdistdir}/source/latex/makebox/makebox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
