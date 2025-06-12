import { ResponseFunctionWebSearch } from "openai/resources/responses/responses.mjs";
import React from "react";

import { FunctionCallMessage } from "@/components/messages/FunctionCallMessage";
import { TextMessage } from "@/components/messages/TextMessage";
import { WebSearchMessage } from "@/components/messages/WebSearchMessage";
import { Message } from "@/lib/types";

type MessageBubbleProps = {
  message: Message;
};

export function MessageBubble({ message }: MessageBubbleProps) {
  switch (message.type) {
    case "function_call":
      return <FunctionCallMessage message={message} />;
    case "function_call_output":
      // already rendered in FunctionCall
      return null;
    case "file_search_call":
      return (
        <div className="flex flex-row gap-2 font-mono text-sm text-gray-500">
          file_search_call: {message.queries.join(", ")}
        </div>
      );
    case "message":
      if (Array.isArray(message.content)) {
        const content = message.content[0];
        if (content.type === "output_text") {
          const isUser = message.role === "user";
          return <TextMessage text={content.text} isUser={isUser} />;
        } else if (content.type === "refusal") {
          return null;
        }
      } else if (typeof message.content === "string") {
        const isUser = message.role === "user";
        return <TextMessage text={message.content} isUser={isUser} />;
      }
      return null;
    case "web_search_call":
      return (
        <WebSearchMessage message={message as ResponseFunctionWebSearch} />
      );
    default:
      console.log("Unknown message type", message);
      return null;
  }
}
