import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Voice agent sample app",
  description:
    "Starter app for building voice agents using the OpenAI Agents SDK",
  icons: {
    icon: "/openai_logo.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased h-full">{children}</body>
    </html>
  );
}
