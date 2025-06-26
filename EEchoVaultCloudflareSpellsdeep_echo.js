

// wallet_sync_do.js

export class WalletSync {
  constructor(state, env) {
    this.state = state;
    this.env = env;
  }

  async fetch(request) {
    const url = new URL(request.url);
    
    if (url.pathname === '/sync') {
      const data = await request.json();
      await this.state.storage.put('latest_trace', data);
      return new Response(JSON.stringify({ status: 'synced', timestamp: data.ts }), { status: 200 });
    }

    if (url.pathname === '/get') {
      const data = await this.state.storage.get('latest_trace');
      return new Response(JSON.stringify(data || { error: 'no data' }), { status: 200 });
    }

    return new Response('WalletSync DO endpoint.', { status: 200 });
  }
}
