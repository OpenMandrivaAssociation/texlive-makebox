Name:		texlive-makebox
Version:	15878
Release:	1
Summary:	Defines a \makebox* command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makebox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebox.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
