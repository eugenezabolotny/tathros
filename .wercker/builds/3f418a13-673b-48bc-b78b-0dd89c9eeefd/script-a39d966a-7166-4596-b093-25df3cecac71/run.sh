set -e
pip_download_cache="$WERCKER_CACHE_DIR/wercker/_pipcache"
mkdir -p ${pip_download_cache}
pip install --cache-dir ${pip_download_cache} -r requirements
