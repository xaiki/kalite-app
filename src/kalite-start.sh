#!/bin/bash

# This function checks if there's any pre-loaded files with
# language (content packs) and/or exercises data (assesment)
# importing them into KA Lite if needed, early returning
# if they were already imported.
install_language_packs() {
    base_dir="/var/lib/kalite"
    temp_dir=$(mktemp -d)
    done_file="${base_dir}/done"
    lang_dir="${base_dir}/content"
    assessment_dir="${base_dir}/assessment"

    if [ ! -d ${base_dir} ]; then
        echo "No '${base_dir}' directory found"
        return;
    fi

    if [ -e ${done_file} ]; then
        echo "Contentpacks and assesment data already imported"
        return
    fi

    # ok we really need to do this, first get some base data working
    kalite manage setup -n

    # check if we have any uninstalled language pack first.
    for f in $(find ${lang_dir} -type f); do
        lang=$(basename $f | sed s/'-minimal'//g | sed s/'.zip'//g)
        kalite manage retrievecontentpack local $lang $f && \
            rm -rf $f
    done

    # assessment data is handled by the package

    touch ${done_file}
}

# This no-op if the language packs were installed.
install_language_packs

# Use --foreground to prevent systemd establishing
# the connection via the socket too early
kalite start --foreground
