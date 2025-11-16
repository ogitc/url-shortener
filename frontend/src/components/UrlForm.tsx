import { useState } from "react";   
import { shorten } from "../lib/api";


export default function UrlForm() {
    const [url, setUrl] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [shortUrl, setShortUrl] = useState<string | null>(null);
  
    async function onSubmit(event: React.FormEvent) {
      event.preventDefault();
      setError(null);
      setShortUrl(null);
      if (!url.trim()) { 
        setError("Please enter a URL");
        return;
      }
      setIsLoading(true);
      try {
        const data = await shorten(url.trim());
        setShortUrl(data.short_url);
      } catch (err: unknown) {
        console.log("error", err);
        setError(err instanceof Error ? err.message : "Failed");
      } finally { 
        setIsLoading(false);
      }
    }
  
    return (
      <main style={{maxWidth: 640, margin: "0 auto", fontFamily: "system-ui",padding: "2rem"}}>
        <h1 style={{textAlign: "center"}}>URL Shortener</h1>
        <form onSubmit={onSubmit} style={{display:"flex", gap:8, justifyContent: "center"}}>
          <input
            style={{flex:1, padding:8}}
            placeholder="https://example.com/very/long/url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
          <button disabled={isLoading} style={{padding:"8px 16px"}}>
            {isLoading ? "Working..." : "Shorten"}
          </button>
        </form>
        {error && <p style={{color:"crimson", textAlign: "center"}}>{error}</p>}
        {shortUrl && (
          <p style={{textAlign: "center"}}>
            Short URL: <code>{shortUrl}</code>{" "}
            <button onClick={() => navigator.clipboard.writeText(shortUrl!)}>Copy</button>
          </p>
        )}
        <p style={{marginTop:24, opacity:.7, textAlign: "center"}}>Paste {shortUrl ?? "<short url>"} into the browser to be redirected.</p>
      </main>
    );
}
