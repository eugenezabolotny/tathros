#!/bin/bash

main() {
  setup_cache
  set +e
  npm_install
  set -e

  success "Finished npm install"
}

setup_cache() {
  mkdir -p "$WERCKER_CACHE_DIR/wercker/npm"
  npm config set cache "$WERCKER_CACHE_DIR/wercker/npm"
}

npm_install() {
  local retries=3;
  for try in $(seq "$retries"); do
    info "Starting npm install, try: $try"
    if [ -n "$WERCKER_NPM_INSTALL_ENVIRONMENT" ]
       then 
         NODE_ENV=$WERCKER_NPM_INSTALL_ENVIRONMENT
         info "Set environment to: $WERCKER_NPM_INSTALL_ENVIRONMENT"
    fi
    npm install $WERCKER_NPM_INSTALL_OPTIONS && return;
  done

  fail "Failed to successfully execute npm install, retries: $retries"
}

main;
