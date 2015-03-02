#!/bin/bash

static_dir="${1}"
dir_name="${2}"

while read file_name ; do
	echo "[[ ${file_name} ]]"
	subst_file="${static_dir}/`basename ${file_name}`"
	diff -q ${file_name} ${subst_file} &> /dev/null
	diff_stat="${?}"
	real_file_path="`readlink -f ${file_name}`"
	real_subst_path="`readlink -f ${subst_file}`"
	if [ "${diff_stat}" = "0" -a "${file_name}" != "${subst_file}" -a "${real_file_path}" == "${real_subst_path}" ] ; then
		echo "OK: ${file_name} and ${subst_file}"
	else
		mv -f "${file_name}" "${subst_file}" && \
		echo "Moved: ${file_name} -> ${subst_file}" && \
		ln -s "../../${subst_file}" "${file_name}" && \
		echo "Symlinked: ${subst_file} -> ${file_name}"
	fi
done < <( find "${dir_name}" -regextype posix-extended -regex '.+/(css|js|common_static)/.+' )

