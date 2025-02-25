import datetime
from typing import List

from google.protobuf.message import Message
from google.protobuf.timestamp_pb2 import Timestamp

from qdrant_client import grpc as grpc
from qdrant_client.conversions.conversion import payload_to_grpc

point_id = grpc.PointId(num=1)
point_id_1 = grpc.PointId(num=2)
point_id_2 = grpc.PointId(uuid="f9bcf279-5e66-40f7-856b-3a9d9b6617ee")

has_id_condition = grpc.HasIdCondition(has_id=[
    point_id,
    point_id_1,
    point_id_2,
])

is_empty = grpc.IsEmptyCondition(key="my.field")

match_keyword = grpc.Match(keyword="hello")
match_integer = grpc.Match(integer=42)
match_bool = grpc.Match(boolean=True)
match_text = grpc.Match(text="hello")

field_condition_match = grpc.FieldCondition(
    key="match_field",
    match=match_keyword
)

range_ = grpc.Range(
    lt=1.0,
    lte=2.0,
    gt=3.0,
    gte=4.0,
)

field_condition_range = grpc.FieldCondition(
    key="match_field",
    range=range_
)

geo_point = grpc.GeoPoint(lon=12.123, lat=78.212)

geo_radius = grpc.GeoRadius(
    center=geo_point,
    radius=10.
)

field_condition_geo_radius = grpc.FieldCondition(
    key="match_field",
    geo_radius=geo_radius
)

geo_bounding_box = grpc.GeoBoundingBox(
    top_left=geo_point,
    bottom_right=geo_point
)

field_condition_geo_bounding_box = grpc.FieldCondition(
    key="match_field",
    geo_bounding_box=geo_bounding_box
)

values_count = grpc.ValuesCount(
    lt=1,
    gt=2,
    gte=3,
    lte=4,
)

field_condition_values_count = grpc.FieldCondition(
    key="match_field",
    values_count=values_count
)

condition_has_id = grpc.Condition(has_id=has_id_condition)
condition_is_empty = grpc.Condition(is_empty=is_empty)

condition_field_match = grpc.Condition(field=field_condition_match)
condition_range = grpc.Condition(field=field_condition_range)
condition_geo_radius = grpc.Condition(field=field_condition_geo_radius)
condition_geo_bounding_box = grpc.Condition(field=field_condition_geo_bounding_box)
condition_values_count = grpc.Condition(field=field_condition_values_count)

filter_ = grpc.Filter(
    must=[
        condition_has_id,
        condition_is_empty,
    ],
    should=[
        condition_field_match,

    ],
    must_not=[
        grpc.Condition(
            filter=grpc.Filter(
                must=[
                    grpc.Condition(
                        field=field_condition_range
                    )
                ]
            )
        )
    ]
)

vector_param = grpc.VectorParams(
    size=100,
    distance=grpc.Distance.Cosine,
)

single_vector_config = grpc.VectorsConfig(params=vector_param)

multiple_vector_config = grpc.VectorsConfig(params_map=grpc.VectorParamsMap(map={"text_vector": vector_param}))

collection_params = grpc.CollectionParams(
    vectors_config=single_vector_config,
    shard_number=10,
    on_disk_payload=True,
)

collection_params_2 = grpc.CollectionParams(
    vectors_config=multiple_vector_config,
    replication_factor=2,
    write_consistency_factor=1
)

hnsw_config = grpc.HnswConfigDiff(
    m=16,
    ef_construct=100,
    full_scan_threshold=10000,
    max_indexing_threads=0,
    on_disk=False,
)

hnsw_config_2 = grpc.HnswConfigDiff(
    m=16,
    ef_construct=100,
    full_scan_threshold=10000,
    max_indexing_threads=2,
    on_disk=True,
    payload_m=32,
)


optimizer_config = grpc.OptimizersConfigDiff(
    deleted_threshold=0.2,
    vacuum_min_vector_number=10000,
    default_segment_number=5,
    max_segment_size=200000,
    memmap_threshold=50000,
    indexing_threshold=10000,
    flush_interval_sec=10,
    max_optimization_threads=0
)

optimizer_config_half = grpc.OptimizersConfigDiff(
    deleted_threshold=0.2,
    vacuum_min_vector_number=10000,
    default_segment_number=5,
    max_segment_size=200000,
)

wal_config = grpc.WalConfigDiff(
    wal_capacity_mb=32,
    wal_segments_ahead=2
)

collection_config = grpc.CollectionConfig(
    params=collection_params,
    hnsw_config=hnsw_config,
    optimizer_config=optimizer_config,
    wal_config=wal_config,
)

payload_value = {
    "int": 1,
    "float": 0.23,
    "keyword": "hello world",
    "bool": True,
    "null": None,
    "dict": {"a": 1, "b": "bbb"},
    "list": [1, 2, 3, 5, 6],
    "list_with_dict": [{}, {}, {}, []],
    "empty_list": [],
}

payload = payload_to_grpc({
    "payload": payload_value
})

single_vector = grpc.Vectors(vector=grpc.Vector(data=[1., 2., 3., 4.]))

scored_point = grpc.ScoredPoint(
    id=point_id,
    payload=payload,
    score=0.99,
    vectors=single_vector,
    version=12
)

create_alias = grpc.CreateAlias(
    collection_name="col1",
    alias_name="col2"
)

search_params = grpc.SearchParams(
    hnsw_ef=128,
)

search_params_2 = grpc.SearchParams(
    exact=True,
)

rename_alias = grpc.RenameAlias(
    old_alias_name="col2",
    new_alias_name="col3"
)

collection_status = grpc.CollectionStatus.Yellow
collection_status_green = grpc.CollectionStatus.Green

optimizer_status = grpc.OptimizerStatus(
    ok=True
)
optimizer_status_error = grpc.OptimizerStatus(
    ok=False,
    error="Error!"
)

payload_schema_keyword = grpc.PayloadSchemaInfo(data_type=grpc.PayloadSchemaType.Keyword)
payload_schema_integer = grpc.PayloadSchemaInfo(data_type=grpc.PayloadSchemaType.Integer)
payload_schema_float = grpc.PayloadSchemaInfo(data_type=grpc.PayloadSchemaType.Float)
payload_schema_geo = grpc.PayloadSchemaInfo(data_type=grpc.PayloadSchemaType.Geo)

collection_info_ok = grpc.CollectionInfo(
    status=collection_status_green,
    optimizer_status=optimizer_status,
    vectors_count=100000,
    segments_count=6,
    config=collection_config,
    payload_schema={
        "keyword_field": payload_schema_keyword,
        "integer_field": payload_schema_integer,
        "float_field": payload_schema_float,
        "geo_field": payload_schema_geo,
    },
)

collection_info = grpc.CollectionInfo(
    status=collection_status,
    optimizer_status=optimizer_status_error,
    vectors_count=100000,
    segments_count=6,
    config=collection_config,
    payload_schema={
        "keyword_field": payload_schema_keyword,
        "integer_field": payload_schema_integer,
        "float_field": payload_schema_float,
        "geo_field": payload_schema_geo,
    },
)

create_collection = grpc.CreateCollection(
    collection_name="my_collection",
    vectors_config=grpc.VectorsConfig(params=grpc.VectorParams(size=100, distance=grpc.Distance.Euclid)),
    hnsw_config=hnsw_config,
    wal_config=wal_config,
    optimizers_config=optimizer_config,
    shard_number=10
)

update_status = grpc.UpdateStatus.Acknowledged

update_result = grpc.UpdateResult(
    operation_id=201,
    status=update_status
)

update_status_completed = grpc.UpdateStatus.Completed

update_result_completed = grpc.UpdateResult(
    operation_id=201,
    status=update_status_completed
)

delete_alias = grpc.DeleteAlias(
    alias_name="col3"
)

point_struct = grpc.PointStruct(
    id=point_id_1,
    vectors=grpc.Vectors(vector=grpc.Vector(data=[1.0, 2.0, -1., -.2])),
    payload=payload_to_grpc({
        "my_payload": payload_value
    }),
)

point_struct_multivec = grpc.PointStruct(
    id=point_id_1,
    vectors=grpc.Vectors(
        vectors=grpc.NamedVectors(
            vectors={
                "image": grpc.Vector(data=[1.0, 2.0, -1., -.2]),
                "text": grpc.Vector(data=[1.0, 2.0, -1., -.2]),
            }
        )
    ),
    payload=payload_to_grpc({
        "my_payload": payload_value
    }),
)

collection_description = grpc.CollectionDescription(
    name="my_col"
)

update_collection = grpc.UpdateCollection(
    collection_name="my_col3",
    optimizers_config=optimizer_config
)

points_ids_list = grpc.PointsIdsList(ids=[point_id, point_id_2, point_id_2])

points_selector_list = grpc.PointsSelector(points=points_ids_list)
points_selector_filter = grpc.PointsSelector(filter=filter_)

alias_operations_create = grpc.AliasOperations(create_alias=create_alias)
alias_operations_rename = grpc.AliasOperations(rename_alias=rename_alias)
alias_operations_delete = grpc.AliasOperations(delete_alias=delete_alias)

with_payload_bool = grpc.WithPayloadSelector(enable=True)
with_payload_include = grpc.WithPayloadSelector(include=grpc.PayloadIncludeSelector(fields=["color", "price"]))
with_payload_exclude = grpc.WithPayloadSelector(exclude=grpc.PayloadExcludeSelector(fields=["color", "price"]))

retrieved_point = grpc.RetrievedPoint(
    id=point_id_1,
    payload=payload_to_grpc({"key": payload_value}),
    vectors=single_vector
)

count_result = grpc.CountResult(count=5)

timestamp = Timestamp()
timestamp.FromDatetime(datetime.datetime.now())

snapshot_description = grpc.SnapshotDescription(
    name="my_snapshot",
    creation_time=timestamp,
    size=100500
)

vector_config = grpc.VectorsConfig(params_map=grpc.VectorParamsMap(map={
    "image": vector_param,
    "text": grpc.VectorParams(
        size=123,
        distance=grpc.Distance.Cosine,
    )
}))

search_points = grpc.SearchPoints(
    collection_name="collection-123",
    vector=[1., 2., 3., 5.],
    filter=filter_,
    limit=100,
    with_payload=with_payload_bool,
    params=search_params,
    score_threshold=0.123,
    offset=10,
    vector_name="abc",
    with_vectors=grpc.WithVectorsSelector(include=grpc.VectorsSelector(names=["abc", "def"])),
)

search_points_all_vectors = grpc.SearchPoints(
    collection_name="collection-123",
    vector=[1., 2., 3., 5.],
    filter=filter_,
    limit=100,
    with_payload=with_payload_bool,
    params=search_params,
    score_threshold=0.123,
    offset=10,
    vector_name="abc",
    with_vectors=grpc.WithVectorsSelector(enable=True),
)

recommend_points = grpc.RecommendPoints(
    collection_name="collection-123",
    positive=[point_id_1, point_id_2],
    negative=[point_id],
    filter=filter_,
    limit=100,
    with_payload=with_payload_bool,
    params=search_params,
    score_threshold=0.123,
    offset=10,
    using="abc",
    with_vectors=grpc.WithVectorsSelector(enable=True),
)

text_index_params_1 = grpc.TextIndexParams(
    tokenizer=grpc.TokenizerType.Prefix,
    lowercase=True,
    min_token_len=2,
    max_token_len=10,
)

text_index_params_2 = grpc.TextIndexParams(
    tokenizer=grpc.TokenizerType.Whitespace,
    lowercase=False,
    max_token_len=10,
)

text_index_params_3 = grpc.TextIndexParams(
    tokenizer=grpc.TokenizerType.Word,
    lowercase=True,
    min_token_len=2,
)

collections_params_diff = grpc.CollectionParamsDiff(
    replication_factor=2,
    write_consistency_factor=2,
)

lookup_location_1 = grpc.LookupLocation(
    collection_name="collection-123",
)

lookup_location_2 = grpc.LookupLocation(
    collection_name="collection-123",
    vector_name="vector-123",
)

read_consistency = grpc.ReadConsistency(
    factor=1,
)

read_consistency_0 = grpc.ReadConsistency(
    type=grpc.ReadConsistencyType.Majority,
)

read_consistency_1 = grpc.ReadConsistency(
    type=grpc.ReadConsistencyType.All,
)

read_consistency_2 = grpc.ReadConsistency(
    type=grpc.ReadConsistencyType.Quorum,
)

ordering_0 = grpc.WriteOrdering(
    type=grpc.WriteOrderingType.Weak,
)

ordering_1 = grpc.WriteOrdering(
    type=grpc.WriteOrderingType.Medium,
)

ordering_2 = grpc.WriteOrdering(
    type=grpc.WriteOrderingType.Strong,
)

fixtures = {
    "CollectionParams": [collection_params, collection_params_2],
    "CollectionConfig": [collection_config],
    "ScoredPoint": [scored_point],
    "CreateAlias": [create_alias],
    "GeoBoundingBox": [geo_bounding_box],
    "SearchParams": [search_params, search_params_2],
    "HasIdCondition": [has_id_condition],
    "RenameAlias": [rename_alias],
    "ValuesCount": [values_count],
    "Filter": [filter_],
    "OptimizersConfigDiff": [
        optimizer_config,
        optimizer_config_half
    ],
    "CollectionInfo": [collection_info, collection_info_ok],
    "CreateCollection": [create_collection],
    "FieldCondition": [
        field_condition_match,
        field_condition_range,
        field_condition_geo_radius,
        field_condition_geo_bounding_box,
        field_condition_values_count
    ],
    "GeoRadius": [geo_radius],
    "UpdateResult": [update_result, update_result_completed],
    "IsEmptyCondition": [is_empty],
    "DeleteAlias": [delete_alias],
    "PointStruct": [point_struct, point_struct_multivec],
    "CollectionDescription": [collection_description],
    "GeoPoint": [geo_point],
    "WalConfigDiff": [wal_config],
    "HnswConfigDiff": [hnsw_config, hnsw_config_2],
    "Range": [range_],
    "UpdateCollection": [update_collection],
    "Condition": [
        condition_field_match,
        condition_range,
        condition_geo_radius,
        condition_geo_bounding_box,
        condition_values_count,
    ],
    "PointsSelector": [
        points_selector_list,
        points_selector_filter
    ],
    "AliasOperations": [
        alias_operations_create,
        alias_operations_rename,
        alias_operations_delete,
    ],
    "Match": [
        match_keyword,
        match_integer,
        match_bool,
        match_text
    ],
    "WithPayloadSelector": [
        with_payload_bool,
        with_payload_include,
        with_payload_exclude,
    ],
    "RetrievedPoint": [
        retrieved_point
    ],
    "CountResult": [count_result],
    "SnapshotDescription": [snapshot_description],
    "VectorParams": [vector_param],
    "VectorsConfig": [single_vector_config, vector_config],
    "SearchPoints": [search_points, search_points_all_vectors],
    "RecommendPoints": [recommend_points],
    "TextIndexParams": [
        text_index_params_1,
        text_index_params_2,
        text_index_params_3,
    ],
    "CollectionParamsDiff": [collections_params_diff],
    "LookupLocation": [lookup_location_1, lookup_location_2],
    "ReadConsistency": [read_consistency, read_consistency_0, read_consistency_1, read_consistency_2],
    "WriteOrdering": [ordering_0, ordering_1, ordering_2],
}


def get_grpc_fixture(model_name: str) -> List[Message]:
    if model_name not in fixtures:
        raise RuntimeError(f"Model {model_name} not found in fixtures")
    return fixtures[model_name]
