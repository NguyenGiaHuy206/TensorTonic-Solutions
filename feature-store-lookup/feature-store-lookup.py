def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    # Write code here
    result = []
    for request in requests:
        user_id = request["user_id"]

        offline_features = feature_store.get(user_id, defaults)

        combined = {
            **offline_features,
            **request["online_features"]
        }

        result.append(combined)

    return result
    pass