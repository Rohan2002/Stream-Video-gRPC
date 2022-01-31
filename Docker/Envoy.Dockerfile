FROM envoyproxy/envoy:v1.20.0

WORKDIR /app
COPY ../envoy.yaml /app/envoy.yaml

CMD /usr/local/bin/envoy -c /app/envoy.yaml -l trace --log-path /tmp/envoy_info.log