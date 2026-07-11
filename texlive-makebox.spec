%global tl_name makebox
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Defines a \makebox* command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makebox
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makebox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makebox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makebox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Define a \makebox* command that does the same as a \makebox command,
except that the width is given by a sample text instead of an explicit
length measure.

