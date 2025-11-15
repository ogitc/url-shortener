export async function shorten(url: string): Promise<{ short_url: string; short_code: string }> {
    const res = await fetch(`${import.meta.env.VITE_API_BASE}/api/shorten`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });
    if (!res.ok) {
      const data = await res.json().catch(() => ({}));
      console.log(data);
      throw new Error(data.detail[0].msg ?? "Request failed");
    }
    return res.json();
  }
  