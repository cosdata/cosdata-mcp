import httpx
from mcp.server.fastmcp import FastMCP
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP("cosdata-docs")

async def fetch_md(url: str) -> str:
    """Helper function to fetch markdown content from URLs."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.text
    except Exception as e:
        logger.error(f"Failed to fetch documentation from {url}: {e}")
        return f"Failed to fetch documentation: {e}"

@mcp.tool()
async def get_cosdata_intro_doc() -> str:
    """Fetches Cosdata's introduction documentation. Use to understand the platform and its purpose."""
    return await fetch_md("https://docs.cosdata.io/md/getting-started/introduction")

@mcp.tool()
async def get_cosdata_installation_doc() -> str:
    """Fetches the installation and quick start guide for Cosdata. Use to set up or initialize a Cosdata project."""
    return await fetch_md("https://docs.cosdata.io/md/getting-started/installation-and-quickstart")

@mcp.tool()
async def get_cosdata_authentication_doc() -> str:
    """Fetches authentication documentation. Use when writing code that accesses the Cosdata API securely."""
    return await fetch_md("https://docs.cosdata.io/md/api/rest-api/authentication")

@mcp.tool()
async def get_cosdata_collections_doc() -> str:
    """Fetches documentation for managing collections in Cosdata. Use when creating or querying collections."""
    return await fetch_md("https://docs.cosdata.io/md/api/rest-api/collections")

@mcp.tool()
async def get_cosdata_transactions_doc() -> str:
    """Fetches documentation for working with transactions. Use when performing batch operations or writes."""
    return await fetch_md("https://docs.cosdata.io/md/api/rest-api/transactions")

@mcp.tool()
async def get_cosdata_search_doc() -> str:
    """Fetches search documentation. Use when performing vector, hybrid, or filtered search queries."""
    return await fetch_md("https://docs.cosdata.io/md/api/rest-api/search")

@mcp.tool()
async def get_cosdata_indexes_doc() -> str:
    """Fetches documentation about creating and managing indexes. Use when configuring vector indexing."""
    return await fetch_md("https://docs.cosdata.io/md/api/rest-api/indexes")

@mcp.tool()
async def get_cosdata_vectors_doc() -> str:
    """Fetches documentation about managing vectors. Use when inserting, updating, or deleting vectors."""
    return await fetch_md("https://docs.cosdata.io/md/api/rest-api/vectors")

@mcp.tool()
async def get_cosdata_versions_doc() -> str:
    """Fetches documentation for versioning in Cosdata. Use when managing record versions or rollbacks."""
    return await fetch_md("https://docs.cosdata.io/md/api/rest-api/versions")

@mcp.tool()
async def get_cosdata_python_sdk_doc() -> str:
    """Fetches Python SDK documentation. Use when writing Python code that interfaces with Cosdata."""
    return await fetch_md("https://docs.cosdata.io/md/api/python-sdk")

@mcp.tool()
async def get_cosdata_node_sdk_doc() -> str:
    """Fetches Node.js SDK documentation. Use when writing Node.js code that interfaces with Cosdata."""
    return await fetch_md("https://docs.cosdata.io/md/api/node-sdk")

@mcp.tool()
async def get_cosdata_vector_search_best_practices_doc() -> str:
    """Fetches best practices for vector search. Use when designing a schema or choosing embeddings."""
    return await fetch_md("https://docs.cosdata.io/md/features/search-relevance")

@mcp.tool()
async def get_cosdata_security_guidelines_doc() -> str:
    """Fetches security best practices. Use when configuring authentication and protecting sensitive data."""
    return await fetch_md("https://docs.cosdata.io/md/api/rest-api/authentication")

@mcp.tool()
async def get_cosdata_github_repo_url() -> str:
    """Returns the URL to Cosdata's GitHub repository."""
    return "https://github.com/cosdata/cosdata"

@mcp.tool()
async def get_cosdata_discord_community_url() -> str:
    """Returns the invite link to the Cosdata community Discord."""
    return "https://discord.gg/XMdtTBrtKT"

if __name__ == "__main__":
    logger.info("Starting Cosdata MCP server...")
    mcp.run(transport="stdio") 