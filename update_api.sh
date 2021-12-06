#! /bin/bash
swagger-codegen generate -i ../billforward/backend/api-v1/target/generated-openapi/non-deprecated.json -l python -DpackageName=billforward
rm -r test/
