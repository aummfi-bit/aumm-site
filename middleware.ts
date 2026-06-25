import { rewrite } from "@vercel/functions";

export const config = {
  matcher: ["/((?!api/).*)\\.md"],
};

export default function middleware(request: Request) {
  const url = new URL(request.url);
  if (!url.searchParams.has("ask")) {
    return;
  }

  const file = url.pathname.replace(/^\//, "");
  const dest = new URL("/api/ask", url.origin);
  url.searchParams.forEach((value, key) => {
    dest.searchParams.set(key, value);
  });
  dest.searchParams.set("file", file);

  return rewrite(dest);
}
