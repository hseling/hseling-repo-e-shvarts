FROM hseling/hseling-api-base:python3.6-alpine3.7 as hseling_web_build

LABEL maintainer="e-shvArts Team <shvarts.edition@gmail.com>"

RUN mkdir /dependencies
COPY ./hseling-web-e-shvarts/requirements.txt /dependencies/requirements.txt
COPY ./hseling-web-e-shvarts/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as hseling_web_production

COPY --from=hseling_web_build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=hseling_web_build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=hseling_web_build /dependencies /dependencies

COPY ./hseling-web-e-shvarts/hseling_web_e_shvarts /app/hseling_web_e_shvarts
COPY ./hseling-web-e-shvarts/hseling_web_e_shvarts/static /app/static
COPY ./hseling-web-e-shvarts/main.py /app/main.py

ENV HSELING_WEB_E_SHVARTS_SETTINGS="/app/hseling_web_e_shvarts/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost:8000/web/healthz || exit 1

EXPOSE 8000
