/*
 * lakeFS API
 *
 * lakeFS HTTP API
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: services@treeverse.io
 * Generated by: https://openapi-generator.tech
 */

use crate::models;

/// StagingMetadata : information about uploaded object
#[derive(Clone, Default, Debug, PartialEq, Serialize, Deserialize)]
pub struct StagingMetadata {
    #[serde(rename = "staging")]
    pub staging: Box<models::StagingLocation>,
    /// unique identifier of object content on backing store (typically ETag)
    #[serde(rename = "checksum")]
    pub checksum: String,
    #[serde(rename = "size_bytes")]
    pub size_bytes: i64,
    #[serde(rename = "user_metadata", skip_serializing_if = "Option::is_none")]
    pub user_metadata: Option<std::collections::HashMap<String, String>>,
    /// Object media type
    #[serde(rename = "content_type", skip_serializing_if = "Option::is_none")]
    pub content_type: Option<String>,
    /// Unix Epoch in seconds.  May be ignored by server.
    #[serde(rename = "mtime", skip_serializing_if = "Option::is_none")]
    pub mtime: Option<i64>,
    #[serde(rename = "force", skip_serializing_if = "Option::is_none")]
    pub force: Option<bool>,
}

impl StagingMetadata {
    /// information about uploaded object
    pub fn new(staging: models::StagingLocation, checksum: String, size_bytes: i64) -> StagingMetadata {
        StagingMetadata {
            staging: Box::new(staging),
            checksum,
            size_bytes,
            user_metadata: None,
            content_type: None,
            mtime: None,
            force: None,
        }
    }
}

