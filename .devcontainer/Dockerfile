ARG BASE_IMAGE=continuumio/miniconda3
FROM ${BASE_IMAGE}

# set proxy
ARG http_proxy
ARG https_proxy
ARG no_proxy

# [Option] Install zsh
ARG INSTALL_ZSH="true"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="true"
# [Option] Enable non-root Docker access in container
ARG ENABLE_NONROOT_DOCKER="true"

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
ARG SOURCE_SOCKET=/var/run/docker-host.sock
ARG TARGET_SOCKET=/var/run/docker.sock
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

COPY .devcontainer/library-scripts/common-debian.sh /tmp/library-scripts/
RUN export http_proxy=$http_proxy && https_proxy=$https_proxy && no_proxy=$no_proxy \
    && export HTTP_PROXY=$http_proxy && HTTPS_PROXY=$https_proxy && NO_PROXY=$no_proxy \
    && apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" \
    # Clean up
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/ \
    && unset http_proxy && unset https_proxy && unset no_proxy \
    && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY

# [Option] Install Docker
ARG INSTALL_DOCKER="true"
COPY .devcontainer/library-scripts/docker-debian.sh /tmp/library-scripts/
RUN export http_proxy=$http_proxy && https_proxy=$https_proxy && no_proxy=$no_proxy \
    && export HTTP_PROXY=$http_proxy && HTTPS_PROXY=$https_proxy && NO_PROXY=$no_proxy \
    && if [ "$INSTALL_DOCKER" = "true" ]; then apt-get update && export DEBIAN_FRONTEND=noninteractive \
    # Use Docker script from script library to set things up
    && bash /tmp/library-scripts/docker-debian.sh "${ENABLE_NONROOT_DOCKER}" "${SOURCE_SOCKET}" "${TARGET_SOCKET}" "${USERNAME}" ; fi \
    # Clean up
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/ \
    && unset http_proxy && unset https_proxy && unset no_proxy \
    && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY

# # [Option] Install RocksDB
# ARG INSTALL_ROCKSDB="true"
# COPY scripts/build-install-rocksdb-debian.sh /tmp/library-scripts/
# RUN export http_proxy=$http_proxy && https_proxy=$https_proxy && no_proxy=$no_proxy \
#     && export HTTP_PROXY=$http_proxy && HTTPS_PROXY=$https_proxy && NO_PROXY=$no_proxy \
#     && if [ "$INSTALL_ROCKSDB" = "true" ]; then apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     # Use Docker script from script library to set things up
#     && bash /tmp/library-scripts/build-install-rocksdb-debian.sh ; fi \
#     # Clean up
#     && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/ \
#     && unset http_proxy && unset https_proxy && unset no_proxy \
#     && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY

# set python/conda related vars
ARG PIP_EXTRA_INDEX_URL="https://pypi.org/simple"
ARG PIP_EXTRA_INDEX_TRUSTED_HOST="pypi.prg"
ARG APP_CONDA_ENV_NAME='base'
ENV APP_CONDA_ENV_NAME=$APP_CONDA_ENV_NAME
ARG CONDA_DIR='/opt/conda'
ENV CONDA_BIN=${CONDA_DIR}/bin/conda
ENV PIP_NO_CACHE_DIR=1
ENV PYTHONDONTWRITEBYTECODE=1

# [Optional] Uncomment to install a different version of Python than the default
# or specify python version in conda environment.yml file
# RUN conda install -y python=3.6

# Setup default python tools in a venv via pipx to avoid conflicts
ENV PIPX_HOME=/usr/local/py-utils \
    PIPX_BIN_DIR=/usr/local/py-utils/bin
ENV PATH=${PATH}:${PIPX_BIN_DIR}
COPY .devcontainer/library-scripts/python-debian.sh /tmp/library-scripts/
RUN export http_proxy=$http_proxy && https_proxy=$https_proxy && no_proxy=$no_proxy \
    && export HTTP_PROXY=$http_proxy && HTTPS_PROXY=$https_proxy && NO_PROXY=$no_proxy \
    && bash /tmp/library-scripts/python-debian.sh "none" "${CONDA_DIR}" "${PIPX_HOME}" "${USERNAME}" "false" \
    # Clean up
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/ \
    && unset http_proxy && unset https_proxy && unset no_proxy \
    && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY

# Copy environment.yml/yaml (if found) to a temp locaition so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
ARG CONDA_TMP='/tmp/conda-tmp'
COPY environment.yml* environment.yaml* .devcontainer/noop.txt ${CONDA_TMP}/
RUN export http_proxy=$http_proxy && https_proxy=$https_proxy && no_proxy=$no_proxy \
    && export HTTP_PROXY=$http_proxy && HTTPS_PROXY=$https_proxy && NO_PROXY=$no_proxy \
    && if [ -f "${CONDA_TMP}/environment.yml" ]; then $CONDA_BIN env update -n $APP_CONDA_ENV_NAME -f ${CONDA_TMP}/environment.yml; fi \
    && if [ -f "${CONDA_TMP}/environment.yaml" ]; then $CONDA_BIN env update -n $APP_CONDA_ENV_NAME -f ${CONDA_TMP}/environment.yaml; fi \
    && $CONDA_BIN init bash --system \
    # Clean up
    && $CONDA_BIN clean --all && rm -rf ${CONDA_TMP} \
    && unset http_proxy && unset https_proxy && unset no_proxy \
    && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY

# # [Option] Install Node.js
# ARG INSTALL_NODE="true"
# ARG NODE_VERSION="none"
# ENV NVM_DIR=/usr/local/share/nvm
# ENV NVM_SYMLINK_CURRENT=true \
#     PATH=${NVM_DIR}/current/bin:${PATH}
# COPY .devcontainer/library-scripts/node-debian.sh /tmp/library-scripts/
# RUN export http_proxy=$http_proxy && https_proxy=$https_proxy && no_proxy=$no_proxy \
#     && export HTTP_PROXY=$http_proxy && HTTPS_PROXY=$https_proxy && NO_PROXY=$no_proxy \
#     && if [ "$INSTALL_NODE" = "true" ]; then bash /tmp/library-scripts/node-debian.sh "${NVM_DIR}" "${NODE_VERSION}" "${USERNAME}"; fi \
#     # Clean up
#     && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/ \
#     && unset http_proxy && unset https_proxy && unset no_proxy \
#     && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY

# [Optional] Uncomment this section to install additional OS packages.
# RUN export http_proxy=$http_proxy && https_proxy=$https_proxy && no_proxy=$no_proxy \
#     && export HTTP_PROXY=$http_proxy && HTTPS_PROXY=$https_proxy && NO_PROXY=$no_proxy \
#     && apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here> \
#     && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
#     && unset http_proxy && unset https_proxy && unset no_proxy \
#     && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY
