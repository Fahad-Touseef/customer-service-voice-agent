import {
  ResponseFunctionToolCall,
  ResponseInputItem,
  ResponseOutputItem,
} from "openai/resources/responses/responses.mjs";

export type ToolCall = ResponseFunctionToolCall & { output?: string };
export type Message = ResponseInputItem | ResponseOutputItem | ToolCall;
